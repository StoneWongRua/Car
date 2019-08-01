from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(231, 75)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/yuancaimaiyi/Desktop/timg.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(2.0)
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
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.Sift = QtWidgets.QAction(MainWindow)
        self.Sift.setObjectName("Sift")
        self.Surf = QtWidgets.QAction(MainWindow)
        self.Surf.setObjectName("Surf")
        self.Daisy = QtWidgets.QAction(MainWindow)
        self.Daisy.setObjectName("Daisy")
        self.openpng = QtWidgets.QAction(MainWindow)
        self.openpng.setObjectName("openpng")
        self.opentif = QtWidgets.QAction(MainWindow)
        self.opentif.setObjectName("opentif")
        self.OpenImage = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/yuancaimaiyi/Desktop/123.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.OpenImage.setIcon(icon1)
        self.OpenImage.setObjectName("OpenImage")
        self.Exit = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("C:/Users/yuancaimaiyi/Desktop/ti.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Exit.setIcon(icon2)
        self.Exit.setObjectName("Exit")
        self.actionRecognize = QtWidgets.QAction(MainWindow)
        self.actionRecognize.setObjectName("actionRecognize")
        self.menuopen.addAction(self.OpenImage)
        self.menuopen.addSeparator()
        self.menuopen.addAction(self.Exit)
        self.menumatching.addSeparator()
        self.menumatching.addAction(self.Sift)
        self.menumatching.addAction(self.Surf)
        self.menumatching.addAction(self.Daisy)
        self.menu.addAction(self.actionRecognize)
        self.menubar.addAction(self.menuopen.menuAction())
        self.menubar.addAction(self.menumatching.menuAction())
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "图像"))
        self.menuopen.setTitle(_translate("MainWindow", "文件"))
        self.menumatching.setTitle(_translate("MainWindow", "特征匹配"))
        self.menu.setTitle(_translate("MainWindow", "人脸识别"))
        self.Sift.setText(_translate("MainWindow", "SIFT "))
        self.Surf.setText(_translate("MainWindow", "SURF"))
        self.Daisy.setText(_translate("MainWindow", "ORB"))
        self.openpng.setText(_translate("MainWindow", "png"))
        self.opentif.setText(_translate("MainWindow", "tif"))
        self.OpenImage.setText(_translate("MainWindow", "openfile"))
        self.OpenImage.setShortcut(_translate("MainWindow", "Ctrl+1"))
        self.Exit.setText(_translate("MainWindow", "exit"))
        self.Exit.setShortcut(_translate("MainWindow", "Ctrl+2"))
        self.actionRecognize.setText(_translate("MainWindow", "Recognize"))