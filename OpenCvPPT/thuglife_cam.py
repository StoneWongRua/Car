import cv2
from PIL import Image
import numpy as np

# 面具地址和分类器的位置

maskPath = "mask.png"
cascPath = r'C:\Users\15845\.ipython\cv2\data\haarcascade_frontalface_default.xml'

# 构建分类器
faceCascade = cv2.CascadeClassifier(cascPath)

# 以pil形式打开
mask = Image.open(maskPath)

def thug_mask(image):

	# 把读取到的帧转换成灰度图，正如我们任务一中提到的脸部检测那样
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	faces = faceCascade.detectMultiScale(gray, 1.15)
	# 把帧转换成pil图片
	background = Image.fromarray(image)

	for (x,y,w,h) in faces:
		# 实时变化面具大小
		resized_mask = mask.resize((w,h), Image.ANTIALIAS)
		offset = (x,y)
		# 把面具放在图像上
		background.paste(resized_mask, offset, mask=resized_mask)

	# 返回帧
	return np.asarray(background)


cap = cv2.VideoCapture('potato.flv')
# cap = cv2.VideoCapture(0)
cap.set(3,320)
cap.set(4,240)


while True:
	ret, frame = cap.read()
	if ret == True:
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		faces = faceCascade.detectMultiScale(gray, 1.15)
		background = Image.fromarray(frame)
		for (x, y, w, h) in faces:
			resized_mask = mask.resize((w, h), Image.ANTIALIAS)
			offset = (x, y)
			background.paste(resized_mask, offset, mask=resized_mask)
		frame = np.asarray(background)
		cv2.imshow('Live', frame)

		if cv2.waitKey(1) == 27:
			break

cap.release()

cv2.destroyAllWindows()
