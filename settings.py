import sys
import os
import shutil
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtWidgets
from PyQt5.Qt import QFileDialog


if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)
    


class Settings(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('settings_window.ui', self)
        self.setWindowTitle("Настройки")
        
        self.open_files = []
        self.file_name = ""

        self.edit_file.clicked.connect(self.open_file)
        self.del_btn.clicked.connect(self.delete_file)
        self.start_btn.clicked.connect(self.start)
    
    def open_file(self):
        try:
            fname = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '')[0]
            if fname.split("/")[-1] not in self.open_files:
                self.open_files.append(fname.split("/")[-1])
                self.files_label.setText(" ; ".join(self.open_files))
                shutil.copy(fname, './dust_photos')
        except FileNotFoundError:
            print("ERROR-01: No file selected to open")

    def delete_file(self):
        fname = QFileDialog.getOpenFileName(self, 'Выбрать картинку', './dust_photos')[0]
        try:
            os.remove(fname)
            self.open_files = os.listdir("./dust_photos")
            self.files_label.setText(" ; ".join(self.open_files))
        except FileNotFoundError:
            print("ERROR-02: No file selected to delete")

    def start(self):
        if self.file_name and os.listdir("./dust_photos"):
            os.system('python ./main.py')
            return self.file_name


if __name__ == '__main__':
    app = QApplication(sys.argv)
    plan = Settings()
    plan.show()
    sys.exit(app.exec_())