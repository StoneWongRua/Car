import cv2
import numpy as np
import matplotlib.pyplot as plt
import scipy
import scipy.stats

def GaussieNoisy(image,sigma):
    row,col,ch= image.shape
    mean = 0
    gauss = np.random.normal(mean,sigma,(row,col,ch))
    gauss = gauss.reshape(row,col,ch)
    noisy = image + gauss
    return noisy.astype(np.uint8)

cat = cv2.imread("cat.jpg")
cat = cv2.resize(cv2.cvtColor(cat,cv2.COLOR_BGR2RGB),(500,500))
plt.imshow(GaussieNoisy(cat,25))
cv2.imwrite("catg.png", GaussieNoisy(cat,25))
cv2.waitKey()
plt.show()