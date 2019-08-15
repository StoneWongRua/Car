import cv2
import numpy as np
from matplotlib import pyplot as plt

# 灰度加载原始RGB图像
img = cv2.imread('bw.png',0)

# 创建一个原始图像的灰度版本
# 所有操作在灰度版本中处理
img2 = img.copy()

# 加载将要搜索的图像模板
template = cv2.imread('moon.png',0)

# 记录图像模板的尺寸
w, h = template.shape[::-1]

# 把OpenCV带有的模板匹配算法存储到一个列表中
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
            'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

for meth in methods:
    img = img2.copy()
    method = eval(meth)

    # 使用matchTemplate对原始灰度图像和图像模板进行匹配
    res = cv2.matchTemplate(img,template,method)

    # 找到最大值和最小值
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    # 对于cv2.TM_SQDIFF及cv2.TM_SQDIFF_NORMED方法min_val越趋近与0匹配度越好，匹配位置取min_loc
    # 对于其他方法max_val越趋近于1匹配度越好，匹配位置取max_loc
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)

    cv2.rectangle(img,top_left, bottom_right, 255, 2)

    # Subplot 多合一显示, xticks、yticks 设置坐标轴刻度
    plt.subplot(121),plt.imshow(res,cmap = 'gray')
    plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(img,cmap = 'gray')
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    plt.suptitle(meth)

    plt.show()