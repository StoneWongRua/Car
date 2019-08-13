import cv2
import numpy


target = cv2.imread("zoom.png")     #读取目标图片
template = cv2.imread("white.png")   #读取模板图片




theight, twidth = template.shape[:2]
result = cv2.matchTemplate(target,template,cv2.TM_SQDIFF_NORMED)
print('result:',result)
#归一化处理
#cv2.normalize( result, result, 0, 1, cv2.NORM_MINMAX, -1 )
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

#绘制矩形边框，将匹配区域标注出来
cv2.rectangle(target,min_loc,(min_loc[0]+twidth,min_loc[1]+theight),(0,0,225),2)

#对于cv2.TM_SQDIFF及cv2.TM_SQDIFF_NORMED方法min_val越趋近与0匹配度越好，匹配位置取min_loc
#对于其他方法max_val越趋近于1匹配度越好，匹配位置取max_loc
strmin_val = str(min_val)
temp_loc = min_loc
other_loc = min_loc
numOfloc = 1


threshold = 0.01                    # 设置匹配阈值为0.01
loc = numpy.where(result<threshold) # 第一次筛选
for other_loc in zip(*loc[::-1]):   # 第二次筛选--将位置偏移小于5个像素的结果舍去
    if (temp_loc[0]+5<other_loc[0])or(temp_loc[1]+5<other_loc[1]):
        numOfloc = numOfloc + 1
        temp_loc = other_loc
        cv2.rectangle(target,other_loc,(other_loc[0]+twidth,other_loc[1]+theight),(0,0,225),2)
str_numOfloc = str(numOfloc)


strText = "MatchResult--MatchingValue="+strmin_val+"--NumberOfPosition="+str_numOfloc
cv2.imshow(strText,target)
cv2.waitKey()
cv2.destroyAllWindows()