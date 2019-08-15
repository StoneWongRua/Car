import cv2

# cap = cv2.VideoCapture('ball.avi')
cap = cv2.VideoCapture(0)
index = 0
imgname = 0
# 用循环不断获取当前帧 处理后显示出来
while True:
    index = index + 1
#   捕获当前帧
    ret,img = cap.read()
#    显示图像
    cv2.imshow('video',img)
#   结束帧捕获的条件
#   等待50ms 即帧频为20fps
    if cv2.waitKey(50) & 0xFF == ord('q'):
        break
# 释放资源
cap.release()
cv2.destroyAllWindows()