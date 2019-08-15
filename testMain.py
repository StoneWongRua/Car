import sys
import json
import base64

from PyQt5 import QtWidgets,QtGui,QtCore
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QTextEdit
import cv2
import numpy as np
from skimage import exposure
import face
from face import facev2
from animal import animal
from flower import flower
from car import car

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(231, 75)
        MainWindow.setGeometry(346, 58, 1124, 896)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)


        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 231, 29))
        self.menubar.setObjectName("menubar")

        self.menuopen = QtWidgets.QMenu(self.menubar)
        self.menuopen.setObjectName("menuopen")
        self.menumatching = QtWidgets.QMenu(self.menubar)
        self.menumatching.setObjectName("menumatching")
        self.menuaudio = QtWidgets.QMenu(self.menubar)
        self.menuaudio.setObjectName("menuaudio")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.statusbar.showMessage("按q退出摄像头窗口")
        MainWindow.setStatusBar(self.statusbar)

        self.tt = QTextEdit()
        MainWindow.setCentralWidget(self.tt)

        # self.addDockWidget(Qt.RightDockWidgetArea, self.dock)


        self.Animal = QtWidgets.QAction(MainWindow)
        self.Animal.setObjectName("Animal")
        self.Face = QtWidgets.QAction(MainWindow)
        self.Face.setObjectName("Face")
        self.Flower = QtWidgets.QAction(MainWindow)
        self.Flower.setObjectName("Flower")
        self.Car = QtWidgets.QAction(MainWindow)
        self.Car.setObjectName("Car")

        self.openpng = QtWidgets.QAction(MainWindow)
        self.openpng.setObjectName("openpng")
        self.opentif = QtWidgets.QAction(MainWindow)
        self.opentif.setObjectName("opentif")
        self.OpenImage = QtWidgets.QAction(MainWindow)
        self.OpenImage.setObjectName("OpenImage")

        self.Exit = QtWidgets.QAction(MainWindow)
        self.Exit.setObjectName("Exit")

        self.Audio = QtWidgets.QAction(MainWindow)
        self.Audio.setObjectName("Audio")

        self.actionRecognize = QtWidgets.QAction(MainWindow)
        self.actionRecognize.setObjectName("actionRecognize")
        self.menuopen.addAction(self.OpenImage)
        self.menuopen.addSeparator()
        self.menuopen.addAction(self.Exit)
        self.menumatching.addSeparator()
        self.menumatching.addAction(self.Animal)
        self.menumatching.addAction(self.Face)
        self.menumatching.addAction(self.Flower)
        self.menumatching.addAction(self.Car)
        self.menuaudio.addSeparator()
        self.menuaudio.addAction(self.Audio)
        self.menu.addAction(self.actionRecognize)
        self.menubar.addAction(self.menuopen.menuAction())
        self.menubar.addAction(self.menumatching.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menuaudio.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "小车功能"))
        self.menuopen.setTitle(_translate("MainWindow", "文本功能"))
        self.menumatching.setTitle(_translate("MainWindow", "图像功能"))
        self.menuaudio.setTitle(_translate("MainWindow", "语音功能"))
        self.menu.setTitle(_translate("MainWindow", "人脸检测"))
        self.Animal.setText(_translate("MainWindow", "动物识别 "))
        self.Face.setText(_translate("MainWindow", "人脸识别"))
        self.Flower.setText(_translate("MainWindow", "植物识别"))
        self.Car.setText(_translate("MainWindow", "车辆识别"))
        self.openpng.setText(_translate("MainWindow", "png"))
        self.opentif.setText(_translate("MainWindow", "tif"))
        self.Audio.setText(_translate("MainWindow", "语音转文字"))
        self.OpenImage.setText(_translate("MainWindow", "文本识别"))

        # self.OpenImage.setShortcut(_translate("MainWindow", "Ctrl+1"))
        self.Exit.setText(_translate("MainWindow", "exit"))
        # self.Exit.setShortcut(_translate("MainWindow", "Ctrl+2"))
        self.actionRecognize.setText(_translate("MainWindow", "Recognize"))



class mywindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(mywindow,self).__init__()
        self.setupUi(self)
        self.OpenImage.triggered.connect(self.open)
        self.Exit.triggered.connect(self.exitP)
        self.f1=[]
        self.Animal.triggered.connect(self.manimal)
        self.Face.triggered.connect(self.mface)
        self.actionRecognize.triggered.connect(self.recognize)
        self.Flower.triggered.connect(self.mflower)
        self.Car.triggered.connect(self.mcar)
        self.Audio.triggered.connect(self.maudio)


    def open(self):
        print(6)

    def exitP(self):
        result = QMessageBox.information(self, "Notice", "Are you sure to exit",QMessageBox.StandardButtons(QMessageBox.Yes | QMessageBox.No))
        if result == QMessageBox.Yes:
            self.close()

    def manimal(self):
        print(5)


    def mface(self):
        print(4)


    def recognize(self):
        print(3)

    def mflower(self):
        print(1)


    def mcar(self):
        print(2)

    def matchIMG(self,im1,im2,kp1,kp2,des1,des2):
        print(3)




    def maudio():
        print("hello audio")
        from audio import SpeechRecognition
        # if a.test(r'C:\Users\15845\Pictures\intel\audio\music\sample-files\16k.wav'):
        #     print("yes")
        # else:
        #     print("no")
        SpeechRecognition.test( r'C:\Users\15845\Pictures\intel\audio\music\sample-files\16k.wav' )




if __name__=="__main__":
    # import sys
    # app = QtWidgets.QApplication(sys.argv)
    # window = mywindow()
    # window.show()
    # app.exec_()
    print("test")
