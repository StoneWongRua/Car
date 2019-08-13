import cv2

# 定义一个无参函数
def cat1():
    # 加载猫脸检测器
    catPath = "C:\ProgramData\Miniconda3\Lib\opencv\data\haarcascades\haarcascade_frontalcatface.xml"
    cat = cv2.CascadeClassifier(catPath)
    # 读取图片并且灰度化
    img = cv2.imread("cat.jpg")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 猫脸检测
    cats = cat.detectMultiScale(
        gray,
        scaleFactor=1.15,
        minNeighbors=5,
        minSize=(3, 3),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    # 框出猫脸并且加上文字说明
    for (x, y, w, h) in cats:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.putText(img, "cat", (x, y - 7), 3, 1.2, (0, 255, 0), 2, cv2.LINE_AA)

    cv2.imshow('cat', img)
    cv2.waitKey(0)


# 定义一个有参函数
def cat(path):
    # -*- coding=utf-8 -*-
    import cv2
    # 加载猫脸检测器
    catPath = "C:\ProgramData\Miniconda3\Lib\opencv\opencv\data\haarcascades\haarcascade_frontalcatface.xml"
    faceCascade = cv2.CascadeClassifier(catPath)
    # 读取图片并灰度化
    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 猫脸检测
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.02,
        minNeighbors=3,
        minSize=(150, 150),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    # 框出猫脸并加上文字说明
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.putText(img, "cat", (x, y - 7), 3, 1.2, (0, 255, 0), 2, cv2.LINE_AA)
    # 显示图片并保存
    cv2.imshow('Cat?', img)
    cv2.imwrite("cat.jpg", img)
    c = cv2.waitKey(0)

if __name__ == '__main__':
    path = "cat.png"
    cat(path)