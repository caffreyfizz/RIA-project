import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import csv, time, cv2, pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR/tesseract.exe'

start = time.time()
colors = ['green', 'red']

# fields for graphs
fig = plt.figure(figsize=(10, 5))
gs = GridSpec(nrows=2, ncols=2, figure=fig)
ax1 = fig.add_subplot(gs[0, 0])
ax2 = fig.add_subplot(gs[1, 0])
ax3 = fig.add_subplot(gs[:, 1])

# select a file
filename = "image 1"
img = Image.open("dust_photos/" + filename + ".png")

# text from picture
text_img = img.crop((0, img.size[1] - img.size[1] / 9.5, img.size[0], img.size[1]))
text = pytesseract.image_to_string(text_img)

# set the received data into variables
izmer = text.split()[-1].replace("u", "μ")
all_len = float(text.split("field: ")[1].split()[0]) * 1000 if izmer == "mm" else float(text.split("field: ")[1].split()[0])

# crop the photo and save in the dust_cropped
img = img.crop((0, 0, img.size[0], img.size[1] - img.size[1]/9.5))
img.save("dust_cropped/"+ filename +"_cropped.png")
img = cv2.imread("dust_cropped/"+ filename +"_cropped.png", cv2.IMREAD_GRAYSCALE)
img = cv2.GaussianBlur(img, (3, 3), 0)

clahe = cv2.createCLAHE(clipLimit=1.0, tileGridSize=(8,8))
img = clahe.apply(img)
_, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
contours1, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_TC89_L1)
ax1.imshow(cv2.cvtColor(thresh, cv2.COLOR_BGR2RGB))

clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
img = clahe.apply(img)
_, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
contours2, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_TC89_L1)

res = cv2.imread("dust_cropped/"+ filename +"_cropped.png")
propr = (all_len) / len(res)

min_area = 0.5

min_area_px = ((np.sqrt((min_area ** 2) / 2) / 2) ** 2 * np.pi) / (propr ** 2)
filtered_contours1 = []
filtered_contours2 = []
for contour in contours1:
    area = cv2.contourArea(contour)
    if area > min_area_px:
        filtered_contours1.append(contour)

for contour in contours2:
    area = cv2.contourArea(contour)
    if area > min_area_px:
        filtered_contours2.append(contour)

# create a CSV file and save it in dust_csv
with open('dust_csv/' + filename + '.csv', 'w', encoding='utf8', newline='') as csv_dust:
    writer = csv.writer(csv_dust, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
    writer.writerow(['coordinates (μm)', 'size (μm)'])
    for coords in filtered_contours1:
        x_values = [vertex[0][0] * propr for vertex in coords]
        y_values = [vertex[0][1] * propr for vertex in coords]
        center = (np.mean(x_values), np.mean(y_values))
        size = np.sqrt(2 * (2 * np.sqrt(cv2.contourArea(coords) * propr ** 2 / np.pi)) ** 2)
        writer.writerow([str(center), size])

# show photos with outlined borders
cv2.drawContours(res, filtered_contours2, -1, (0, 0, 255), 2)
cv2.drawContours(res, filtered_contours1, -1, (0, 255, 0), 2)
ax2.imshow(cv2.cvtColor(res, cv2.COLOR_BGR2RGB))

# create a histogram
sizes1 = []
sizes2 = []
for i in filtered_contours1:
   sizes1.append(np.sqrt(2 * (2 * np.sqrt(cv2.contourArea(i) * propr ** 2 / np.pi)) ** 2))
for i in filtered_contours2:
   sizes2.append(np.sqrt(2 * (2 * np.sqrt(cv2.contourArea(i) * propr ** 2 / np.pi)) ** 2))
ax3.hist([sizes1, sizes2], bins=50, color = colors, log=True, alpha = 0.5, label=['Уверен', 'Не уверен']) 
ax3.set_title("Количество пыли (μm) " + (f" [min size={min_area} μm]" if min_area != 0 else ""))
plt.legend()

sure = len(filtered_contours1)
not_sure = len(filtered_contours2) - sure

end = time.time() - start

# information output
final_txt = f'''
Размер экрана: {all_len} μm
Коэффициент (μm в пикселе): {str(propr)}
Время работы проргаммы: {round(end, 3)} с
Количество пыли в которой уверен: {sure}
Количество пыли в которой НЕ уверен: {not_sure}'''

fig.text(0.05, 0.9, final_txt, fontsize = 8, color = "black")

plt.show()