import math
from PyQt5.QtWidgets import *
from calculator import Ui_MainWindow

class main(QMainWindow):
    def __init__(self) -> None:
        super().__init()
        self.qtTasarim = Ui_MainWindow()
        self.qtTasarim.setupUi(self)
        self.qtTasarim.pushButton.clicked.connect(self.bolme)
        self.qtTasarim.pushButton_0.clicked.connect(self.EkleTikla)
        self.qtTasarim.pushButton_10.clicked.connect(self.EkleTikla)
        self.qtTasarim.pushButton_11.clicked.connect(self.toplama)
        self.qtTasarim.pushButton_12.clicked.connect(self.EkleTikla)
        self.qtTasarim.pushButton_13.clicked.connect(self.cikarma)
        self.qtTasarim.pushButton_14.clicked.connect(self.EkleTikla)
        self.qtTasarim.pushButton_16.clicked.connect(self.sil)
        self.qtTasarim.pushButton_2.clicked.connect(self.EkleTikla)
        self.qtTasarim.pushButton_4.clicked.connect(self.EkleTikla)
        self.qtTasarim.pushButton_5.clicked.connect(self.EkleTikla)
        self.qtTasarim.pushButton_9.clicked.connect(self.EkleTikla)
        self.qtTasarim.pushButton_8.clicked.connect(self.EkleTikla)
        self.qtTasarim.pushButton_7.clicked.connect(self.carpma)
        self.qtTasarim.pushButton_6.clicked.connect(self.EkleTikla)
    def EkleTikla(self):
        self.qtTasarim.lineEdit

