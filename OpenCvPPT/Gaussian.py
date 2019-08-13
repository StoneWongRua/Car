'''
图像均值平滑滤波
'''

import numpy as np
import cv2

image = cv2.imread('zhuyin.jpeg',0)
#image = cv2.resize(cv2.cvtColor(image,cv2.COLOR_BGR2RGB),(100,100))

pepper = cv2.imread("pepper.png")
# pepper = cv2.resize(cv2.cvtColor(pepper,cv2.COLOR_BGR2RGB),(200,200))



# 算术均值滤波
blurred = np.hstack(
    [cv2.blur(image,(3,3)),
     cv2.blur(image,(5,5)),
     cv2.blur(image,(7,7))
    ])
cv2.imshow("Averaged",blurred)


#高斯滤波
blurred = np.hstack(
    [cv2.GaussianBlur(image,(3,3),0),
     cv2.GaussianBlur(image,(5,5),0),
     cv2.GaussianBlur(image,(7,7),0)
     ])
cv2.imshow("Gaussian",blurred)





#中值滤波
blurred = np.hstack(
    [cv2.medianBlur(image,3),
    cv2.medianBlur(image,5),
    cv2.medianBlur(image,7)
    ])
cv2.imshow("Median",blurred)


#双边滤波
blurred = np.hstack([cv2.bilateralFilter(image,5,21,21),
                     cv2.bilateralFilter(image,7, 31, 31),
                     cv2.bilateralFilter(image,9, 41, 41)
                     ])
cv2.imshow("Bilateral",blurred)

cv2.waitKey(0)
