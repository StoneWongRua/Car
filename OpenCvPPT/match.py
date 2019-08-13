# 导入所需库文件
import cv2
import numpy as np

# 加载原始RGB图像
img_rgb = cv2.imread("bw.png")

# 创建一个原始图像的灰度版本
# 所有操作在灰度版本中处理
# 然后在RGB图像中使用相同坐标还原

img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

# 加载将要搜索的图像模板
template = cv2.imread('moon.png',0)

# 记录图像模板的尺寸
w, h = template.shape[::-1]

# 使用matchTemplate对原始灰度图像和图像模板进行匹配
res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)


# 设定阈值
threshold = 0.7
# res大于70%
loc = np.where(res >= threshold)

# 使用灰度图像中的坐标对原始RGB图像进行标记
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (255,  255, 0), 5)

# 显示图像
cv2.imshow('Detected',img_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()



