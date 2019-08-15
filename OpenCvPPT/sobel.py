import cv2

img = cv2.imread('desk.png', 0)
img = cv2.resize(img,(300,300), cv2.INTER_CUBIC)
# cv2.CV_64F 出图像的深度 数据类型 可以使用 -1, 与原图像保持一致 np.uint8
# 参数 1,0 为只在 x 方向求一 导数 最大可以求 2 导数。
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
cv2.imshow("sobelx", sobelx)
# 参数 0,1 为只在 y 方向求一 导数 最大可以求 2 导数。
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)
cv2.imshow("sobely", sobely)
cv2.waitKey(0)

