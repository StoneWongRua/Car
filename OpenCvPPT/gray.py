import cv2

cat = cv2.imread('cat.png') # 读取一张图片
gray = cv2.cvtColor(cat, cv2.COLOR_BGR2GRAY) # 转换为灰度图

cv2.imshow("cat", cat) # 显示原图
cv2.imshow("gray", gray) # 显示灰度图
cv2.imwrite("test.png", gray) # 保存灰度图
cv2.waitKey(0)

