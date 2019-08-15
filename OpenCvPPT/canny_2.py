import cv2

img = cv2.imread('desk.png', 1)
cv2.namedWindow('window')

def track_back(x):
    pass

# 创建滑动条
cv2.createTrackbar('maxVal', 'window', 100, 255, track_back)
cv2.createTrackbar('minVal', 'window', 200, 255, track_back)

while(True):
    # 获取滑动条的值
    max_val = cv2.getTrackbarPos('maxVal', 'window')
    min_val = cv2.getTrackbarPos('minVal', 'window')

    edges = cv2.Canny(img, min_val, max_val)
    cv2.imshow('window', edges)
    # 按下ESC键退出
    if cv2.waitKey(30) == 27:
        break


