from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import json
import base64
from PIL import Image
import time, threading

from PyQt5 import  QtWidgets,QtGui,QtCore
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QTextEdit
import cv2
import numpy as np
from skimage import exposure
import face
from face import facev2
from animal import animal
from flower import flower
from car import car

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

        self.IDCard = QtWidgets.QAction(MainWindow)
        self.IDCard.setObjectName("IDCard")

        self.Exit = QtWidgets.QAction(MainWindow)
        self.Exit.setObjectName("Exit")



        self.Audio = QtWidgets.QAction(MainWindow)
        self.Audio.setObjectName("Audio")

        self.Weather = QtWidgets.QAction(MainWindow)
        self.Weather.setObjectName("Weather")

        self.Translate = QtWidgets.QAction(MainWindow)
        self.Translate.setObjectName("Translate")

        self.actionRecognize = QtWidgets.QAction(MainWindow)
        self.actionRecognize.setObjectName("actionRecognize")

        self.menuopen.addAction(self.OpenImage)
        self.menuopen.addAction(self.IDCard)
        self.menuopen.addSeparator()
        self.menuopen.addAction(self.Exit)

        self.menumatching.addSeparator()
        self.menumatching.addAction(self.Animal)
        self.menumatching.addAction(self.Face)
        self.menumatching.addAction(self.Flower)
        self.menumatching.addAction(self.Car)
        self.menuaudio.addSeparator()
        self.menuaudio.addAction(self.Audio)
        self.menuaudio.addAction ( self.Weather )
        self.menuaudio.addAction ( self.Translate )
        self.menu.addAction(self.actionRecognize)
        self.menubar.addAction(self.menuopen.menuAction())
        self.menubar.addAction(self.menumatching.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menuaudio.menuAction())

        self.timer = QTimer ( self )

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
        self.Weather.setText(_translate("MainWindow", "天气预报"))
        self.Translate.setText ( _translate ( "MainWindow", "语音翻译" ) )
        self.OpenImage.setText(_translate("MainWindow", "文本识别"))
        self.IDCard.setText ( _translate ( "MainWindow", "身份证识别" ) )
        # self.OpenImage.setShortcut(_translate("MainWindow", "Ctrl+1"))
        self.Exit.setText(_translate("MainWindow", "exit"))
        # self.Exit.setShortcut(_translate("MainWindow", "Ctrl+2"))
        self.actionRecognize.setText(_translate("MainWindow", "表情包"))



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
        self.Weather.triggered.connect(self.mweather)
        self.Translate.triggered.connect(self.mtranslate)
        self.IDCard.triggered.connect ( self.midcard )

        self._mutex = QtCore.QMutex ()



    def open(self):
        # file,ok=QFileDialog.getOpenFileName(self,"打开",None,"*.jpg;;*.png;;*.tif;;*.bmp")
        # self.f1.append(file)
        # self.statusbar.showMessage(file)
        self._mutex.lock ()
        from text import text81

        # from pprint import pprint
        # pprint(text81.detect(path))
        # data = text81.detect(path)
        # for word in range(0, len(data)):
        #     print(data)
        # print(data)

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
                fname = 'text.jpg'
                #           写入截图
                cv2.imwrite(fname, img)
                print(fname + ' saved')
                img = fname
                text81.detect(fname)
                data = text81.detect(fname)
                for i in data:
                    for value in i.values ():
                        self.tt.append(str(value))

                index = 0
            if cv2.waitKey(50) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
        self._mutex.unlock ()

    def exitP(self):
        self._mutex.lock ()
        result=QMessageBox.information(self,"Notice","Are you sure to exit",QMessageBox.StandardButtons(QMessageBox.Yes|QMessageBox.No))
        if result==QMessageBox.Yes:
            self.close()
            self._mutex.unlock ()


    def manimal(self):
        self._mutex.lock ()
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
        self._mutex.unlock ()


    def mface(self):
        self._mutex.lock ()
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


                            self.tt.append("编号" + chr(num) + "   性别: " + gender + " 年龄: " + str(face["age"]))
                            self.tt.append("\n--------------------------------------------------")
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
        self._mutex.unlock ()


    def recognize(self):
        self._mutex.lock ()
        # face=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        # face.load(r'C:\Users\15845\.ipython\cv2\data\haarcascade_frontalface_default.xml')
        # cap=cv2.VideoCapture(0)
        # self.statusbar.showMessage("若想退出人脸识别视频流，则需要按下键盘的Esc键")
        # while 1:
        #     ret,frame=cap.read()
        #     frame=exposure.adjust_gamma(frame,0.5)
        #     grayframe=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        #     faces=face.detectMultiScale(grayframe,1.3,5)
        #     for (x,y,w,h) in faces:
        #         cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        #     cv2.imshow('img',frame)
        #     k=cv2.waitKey(10)
        #     if k==27:
        #         break
        # cv2.destroyAllWindows()
        self.statusbar.showMessage ( "若想退出人脸识别视频流，则需要按下键盘的Esc键" )
        maskPath = "mask.png"
        cascPath = r'C:\Users\15845\.ipython\cv2\data\haarcascade_frontalface_default.xml'

        # 构建分类器
        faceCascade = cv2.CascadeClassifier ( cascPath )

        # 以pil形式打开
        mask = Image.open ( maskPath )

        def thug_mask(image):

            # 把读取到的帧转换成灰度图，正如我们任务一中提到的脸部检测那样
            gray = cv2.cvtColor ( image, cv2.COLOR_BGR2GRAY )
            faces = faceCascade.detectMultiScale ( gray, 1.15 )
            # 把帧转换成pil图片
            background = Image.fromarray ( image )

            for (x, y, w, h) in faces:
                # 实时变化面具大小
                resized_mask = mask.resize ( (w, h), Image.ANTIALIAS )
                offset = (x, y)
                # 把面具放在图像上
                background.paste ( resized_mask, offset, mask=resized_mask )

            # 返回帧
            return np.asarray ( background )

        cap = cv2.VideoCapture ( 0 )
        # cap = cv2.VideoCapture(0)
        cap.set ( 3, 320 )
        cap.set ( 4, 240 )

        while True:
            ret, frame = cap.read ()
            if ret == True:
                gray = cv2.cvtColor ( frame, cv2.COLOR_BGR2GRAY )
                faces = faceCascade.detectMultiScale ( gray, 1.15 )
                background = Image.fromarray ( frame )
                for (x, y, w, h) in faces:
                    resized_mask = mask.resize ( (w, h), Image.ANTIALIAS )
                    offset = (x, y)
                    background.paste ( resized_mask, offset, mask=resized_mask )
                frame = np.asarray ( background )
                cv2.imshow ( 'Live', frame )

                if cv2.waitKey ( 1 ) == 27:
                    break

        cap.release ()

        cv2.destroyAllWindows ()
        self._mutex.unlock ()


    def mflower(self):
        self._mutex.lock ()
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
                fname = 'flower.jpg'
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
        self._mutex.unlock ()


    def mcar(self):
        self._mutex.lock ()
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
        self._mutex.unlock ()


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

    def luyin(self):
        """PyAudio example: Record a few seconds of audio and save to a WAVE file."""

        import pyaudio
        import wave

        CHUNK = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 8000
        RECORD_SECONDS = 3
        WAVE_OUTPUT_FILENAME = "111.wav"

        p = pyaudio.PyAudio ()

        stream = p.open ( format=FORMAT,
                          channels=CHANNELS,
                          rate=RATE,
                          input=True,
                          frames_per_buffer=CHUNK )

        self.tt.append ( "* recording" )

        frames = []

        for i in range ( 0, int ( RATE / CHUNK * RECORD_SECONDS ) ):
            data = stream.read ( CHUNK )
            frames.append ( data )

        self.tt.append  ( "* done recording" )

        stream.stop_stream ()
        stream.close ()
        p.terminate ()

        wf = wave.open ( WAVE_OUTPUT_FILENAME, 'wb' )
        wf.setnchannels ( CHANNELS )
        wf.setsampwidth ( p.get_sample_size ( FORMAT ) )
        wf.setframerate ( RATE )
        wf.writeframes ( b''.join ( frames ) )
        wf.close ()
        return WAVE_OUTPUT_FILENAME


    def maudio(self):
        path = r'C:\Users\15845\Pictures\intel\audio\music\sample-files\16k.wav'

        import winsound
        duration = 100  # millisecond
        freq = 440  # Hz
        winsound.Beep ( freq, duration )
        path = self.luyin()
        from audio import SpeechRecognition
        try:
            self.tt.append ( SpeechRecognition.test ( path ) )
            result = SpeechRecognition.test ( path )
        except KeyError:
            self.tt.append("?")
            result = False
        finally:
            print("test")
        winsound.Beep ( freq, duration )
        return result

    def mweather(self):

        # from audio import luyin
        # self.tt.append ("开始录音")
        # path = luyin.luyin()
        # self.tt.append ("结束录音")
        from audio import weather
        # print(self.maudio())
        from audio import SpeechRecognition
        path = r"C:\Users\15845\Pictures\intel\output.wav"
        result = SpeechRecognition.test ( path )
        if SpeechRecognition.weather(path):
            try:
                self.tt.append ( weather.weather_analyse ( "auto_ip" ) )
            except KeyError:
                self.tt.append ( "error, 重新开始录音" )
                self.mweather()
            finally:
                print('wrong')


    def mtranslate(self):
        from audio import youdao
        app_key_data = {'key': '61555165', 'keyfrom': 'pythoncontent1111'}
        m = youdao.youdao_fanyi ( app_key_data )
        m.analysis_json ()
        self.tt.append (str(m.analysis_json ()))



    def midcard(self):
        self._mutex.lock ()
        from text import idcard
        cap = cv2.VideoCapture ( 0 )
        index = 0
        imgname = 0
        # 用循环不断获取当前帧 处理后显示出来
        while True:
            index = index + 1
            #   捕获当前帧
            ret, img = cap.read ()
            #    显示图像
            cv2.imshow ( 'video', img )
            #   每5秒保存一张截图
            if index == 25:
                imgname = imgname + 1
                if imgname >= 5:
                    imgname = 0
                #           文件名字符串拼接
                fname = 'idcard.jpg'
                #           写入截图
                cv2.imwrite ( fname, img )
                print ( fname + ' saved' )
                img = fname

                result = idcard.IDCardRecognizer ( api_key='xXDugOa8S6GpMHfPK4OrXotZ',
                                                   secret_key='yzZps0FwcYVuigpB6SVz8mI6Q0DwZIhs' ).detect ( img )
                if str ( result ) != "None":
                    self.tt.append ( str ( result ) )
                else:
                    self.tt.append ( "检测不到身份证\n--------------------------------------\n" )

                index = 0
            if cv2.waitKey ( 50 ) & 0xFF == ord ( 'q' ):
                break

        cap.release ()
        cv2.destroyAllWindows ()
        self._mutex.unlock ()




if __name__=="__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    window=mywindow()
    window.show()
    app.exec_()

