# RIA 
Reactor image analysis - An algorithm designed for analyzing an image in a thermonuclear reactor. The main task was to recognize radioactive dust particles in the picture, count their number, determine their sizes, and create a table and a diagram.

## Content
- [Technologies](#Technologies)
- [Beginning of work](#Beginning-of-work)
- [Principle of operation](#Principle-of-operation)
- [Result](#Result)
- [The project team](#The-project-team)
- [License](#License)

## Technologies
- [OpenCV](https://pypi.org/project/opencv-python/)
- [pytesseract](https://pypi.org/project/pytesseract/)
- [csv](https://docs.python.org/3/library/csv.html)
- [PIL](https://pypi.org/project/pillow/)
- [matplotlib](https://matplotlib.org/)
- [numpy](https://numpy.org/)

## Beginning of work
Run the settings.py file and follow the instructions on the screen. After the start, you will be shown the results of the algorithm, and the cropped photo and table will be saved in the appropriate folders of the program.

Install the required libraries using the command:
```sh
pip install -r requirements.txt
```

Also install tesseract-ocr using the link:
```sh
https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-5.3.3.20231005.exe
```
⚠Attention! You need to install tesseract-ocr along the following path:
```sh
C:\Program Files\
```

## Principle of operation
- Uploading a photo
- Selection of minimum particle size
- Entering the file name
- Counting the number of particles you are sure of
- Counting the number of particles which is unsure
- Graphing
- Displaying the outlines of recognized particles
- Information output

## Result
You will see the original image and the image with outlines. To the right of the images there will be a graph of particle concentration, and in the upper left corner there will be general information about the operation of the algorithm. The cropped image and table with coordinates will be loaded into the corresponding folders in the file of the executable program.

## The project team

- [Юсько Никита Витальевич](https://github.com/caffreyfizz/)
- [Диб Наталья Владимировна](https://imc.edu.ru/%D1%81%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D1%8F-%D0%BE%D0%B1-%D0%BE%D0%BE/%D1%80%D1%83%D0%BA%D0%BE%D0%B2%D0%BE%D0%B4%D1%81%D1%82%D0%B2%D0%BE-%D0%BF%D0%B5%D0%B4%D1%81%D0%BE%D1%81%D1%82%D0%B0%D0%B2/%D0%B4%D0%B8%D0%B1-%D0%BD%D0%B0%D1%82%D0%B0%D0%BB%D1%8C%D1%8F-%D0%B2%D0%BB%D0%B0%D0%B4%D0%B8%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%BD%D0%B0)

## License
The software code is distributed under the MIT license. All rights reserved.