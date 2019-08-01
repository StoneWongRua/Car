from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import json
import base64
IS_PY3 = sys.version_info.major == 3
if IS_PY3:
    from urllib.request import urlopen
    from urllib.request import Request
    from urllib.error import URLError
    from urllib.parse import urlencode
    from urllib.parse import quote_plus
else:
    print("wrong")
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(231, 75)
        MainWindow.setGeometry(300, 300, 550, 350)
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
        self.menu.addAction(self.actionRecognize)
        self.menubar.addAction(self.menuopen.menuAction())
        self.menubar.addAction(self.menumatching.menuAction())
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "小车功能"))
        self.menuopen.setTitle(_translate("MainWindow", "语音功能"))
        self.menumatching.setTitle(_translate("MainWindow", "图像功能"))
        self.menu.setTitle(_translate("MainWindow", "人脸检测"))
        self.Animal.setText(_translate("MainWindow", "动物识别 "))
        self.Face.setText(_translate("MainWindow", "人脸识别"))
        self.Flower.setText(_translate("MainWindow", "植物识别"))
        self.Car.setText(_translate("MainWindow", "车辆识别"))
        self.openpng.setText(_translate("MainWindow", "png"))
        self.opentif.setText(_translate("MainWindow", "tif"))
        self.OpenImage.setText(_translate("MainWindow", "openfile"))
        # self.OpenImage.setShortcut(_translate("MainWindow", "Ctrl+1"))
        self.Exit.setText(_translate("MainWindow", "exit"))
        # self.Exit.setShortcut(_translate("MainWindow", "Ctrl+2"))
        self.actionRecognize.setText(_translate("MainWindow", "Recognize"))

from PyQt5 import  QtWidgets,QtGui,QtCore
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QTextEdit
import cv2
import numpy as np
from skimage import exposure
import face
from face import facev2
from animal import animal
from flower import flower
from car import car

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


    def open(self):
        file,ok=QFileDialog.getOpenFileName(self,"打开",None,"*.jpg;;*.png;;*.tif;;*.bmp")
        self.f1.append(file)
        self.statusbar.showMessage(file)
    def exitP(self):
        result=QMessageBox.information(self,"Notice","Are you sure to exit",QMessageBox.StandardButtons(QMessageBox.Yes|QMessageBox.No))
        if result==QMessageBox.Yes:
            self.close()


    def manimal(self):
        recognizer = animal.AnimalRecognizer(api_key='PtGR84MlaNQL6KLPeB73A4Xd', secret_key='Ze0KrGXEtyLykKAMbAn09xRWIfXsTjmc')
        cap = cv2.VideoCapture(0)
        index = 0
        imgname = 0
        # 用循环不断获取当前帧 处理后显示出来
        while True:
            index = index + 1
            #   捕获当前帧
            ret, img = cap.read()
            #    显示图像
            cv2.imshow('video', img)
            #   每5秒保存一张截图
            if index == 25:
                imgname = imgname + 1
                if imgname >= 5:
                    imgname = 0
                #           文件名字符串拼接
                fname = 'animal.jpg'
                #           写入截图
                cv2.imwrite(fname, img)
                print(fname + ' saved')
                img = fname
                recognizer.detect(img)
                self.tt.append(recognizer.detect(img))
                index = 0
            if cv2.waitKey(50) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()


    def mface(self):
        cap = cv2.VideoCapture(0)
        index = 0
        imgname = 0
        # 用循环不断获取当前帧 处理后显示出来
        while True:
            index = index + 1
            #   捕获当前帧
            ret, img = cap.read()
            #    显示图像
            cv2.imshow('video', img)
            #   每5秒保存一张截图
            if index == 10:
                imgname = imgname + 1
                if imgname >= 5:
                    imgname = 0
                #           文件名字符串拼接
                fname = 'face.jpg'
                #           写入截图
                cv2.imwrite(fname, img)
                print(fname + ' saved')
                img = fname
                # get access token
                token = facev2.fetch_token()

                # concat url
                url = facev2.FACE_DETECT + "?access_token=" + token

                file_content = facev2.read_file(img)
                response = facev2.request(url, urlencode(
                    {
                        'image': base64.b64encode(file_content),
                        'image_type': 'BASE64',
                        'face_field': 'gender,age',
                        'max_face_num': 10
                    }))

                data = json.loads(response)
                num = 65;

                if data["error_code"] == 0:
                    face_num = data["result"]["face_num"]
                    if face_num == 0:
                        # could not find face
                        self.statusbar.showMessage("no face in the picture")
                    else:
                        # get face list
                        face_list = data["result"]["face_list"]
                        for face in face_list:
                            # male face
                            if face["gender"]["type"] == "male":
                                gender = "男"
                            # female face
                            if face["gender"]["type"] == "female":
                                gender = "女"


                            self.tt.append("顾客" + chr(num) + "   性别: " + gender + " 年龄: " + str(face["age"]))
                            #self.tt.append("你点我啦！")
                            num = num + 1

                else:
                    # print error response
                    print(response)
                index = 0
            if cv2.waitKey(50) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()


    def recognize(self):
        face=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        face.load(r'C:\Users\15845\.ipython\cv2\data\haarcascade_frontalface_default.xml')
        cap=cv2.VideoCapture(0)
        self.statusbar.showMessage("若想退出人脸识别视频流，则需要按下键盘的Esc键")
        while 1:
            ret,frame=cap.read()
            frame=exposure.adjust_gamma(frame,0.5)
            grayframe=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            faces=face.detectMultiScale(grayframe,1.3,5)
            for (x,y,w,h) in faces:
                cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            cv2.imshow('img',frame)
            k=cv2.waitKey(10)
            if k==27:
                break
        cv2.destroyAllWindows()


    def mflower(self):
        recognizer = flower.PlantRecognizer(api_key='PtGR84MlaNQL6KLPeB73A4Xd', secret_key='Ze0KrGXEtyLykKAMbAn09xRWIfXsTjmc')
        cap = cv2.VideoCapture(0)
        index = 0
        imgname = 0
        # 用循环不断获取当前帧 处理后显示出来
        while True:
            index = index + 1
            #   捕获当前帧
            ret, img = cap.read()
            #    显示图像
            cv2.imshow('video', img)
            #   每5秒保存一张截图
            if index == 25:
                imgname = imgname + 1
                if imgname >= 5:
                    imgname = 0
                #           文件名字符串拼接
                fname = 'animal.jpg'
                #           写入截图
                cv2.imwrite(fname, img)
                print(fname + ' saved')
                img = fname
                recognizer.detect(img)
                self.tt.append(recognizer.detect(img))
                index = 0
            if cv2.waitKey(50) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()


    def mcar(self):
        recognizer = car.CarRecognizer(api_key='PtGR84MlaNQL6KLPeB73A4Xd',
                                     secret_key='Ze0KrGXEtyLykKAMbAn09xRWIfXsTjmc')
        cap = cv2.VideoCapture(0)
        index = 0
        imgname = 0
        # 用循环不断获取当前帧 处理后显示出来
        while True:
            index = index + 1
            #   捕获当前帧
            ret, img = cap.read()
            #    显示图像
            cv2.imshow('video', img)
            #   每5秒保存一张截图
            if index == 25:
                imgname = imgname + 1
                if imgname >= 5:
                    imgname = 0
                #           文件名字符串拼接
                fname = 'car.jpg'
                #           写入截图
                cv2.imwrite(fname, img)
                print(fname + ' saved')
                img = fname
                recognizer.detect(img)
                self.tt.append(recognizer.detect(img))
                index = 0
            if cv2.waitKey(50) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

    def matchIMG(self,im1,im2,kp1,kp2,des1,des2):
        FLANN_INDEX_KDTREE=0
        index_p=dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
        searth_p=dict(checks=50)
        flann=cv2.FlannBasedMatcher(index_p,searth_p)
        matches=flann.knnMatch(des1,des2,k=2)
        good =[]
        pts1=[]
        pts2=[]
        for i,(m,n) in enumerate(matches):
            if m.distance<0.6*n.distance:
                good.append(m)
                pts1.append(kp1[m.queryIdx].pt)
                pts2.append(kp2[m.trainIdx].pt)
        pts1=np.float32(pts1)
        pts2=np.float32(pts2)
        F,mask=cv2.findFundamentalMat(pts1,pts2,cv2.RANSAC,0.01)
        pts1_1=pts1[mask.ravel()==1]
        pts2_2=pts2[mask.ravel()==1]
        pts2_new=pts2_2.copy()
        for i in range(len(pts2_2)):
            pts2_new[i,0]=pts2_new[i,0]+np.float32(im1.shape[1])
        def appendimage(im1,im2):
            r1=im1.shape[0]
            r2=im2.shape[0]
            if r1<r2:
                img=np.zeros((r2-r1,im1.shape[1]),np.uint8)
                im1_1=np.vstack((im1,img))
                im3=np.hstack((im1_1,im2))
            else:
                img=np.zeros((r1-r2,im2.shape[1]),np.uint8)
                im2_2=np.vstack((im2,img))
                im3=np.hstack((im1,im2_2))
            return im3
        im3=appendimage(im1,im2)
        for i in range(len(pts1_1)):
            cv2.line(im3,tuple(pts1_1[i]),tuple(pts2_new[i]),255,2)
        return im3


if __name__=="__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    window=mywindow()
    window.show()
    app.exec_()