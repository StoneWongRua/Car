import cv2
import numpy as np
peppers = cv2.imread("shrink.png", 0)
row, column = peppers.shape
noise_salt = np.random.randint(0, 256, (row, column))
noise_pepper = np.random.randint(0, 256, (row, column))
rand = 0.1
noise_salt = np.where(noise_salt < rand * 256, 255, 0)
noise_pepper = np.where(noise_pepper < rand * 256, -255, 0)

peppers.astype("float")
noise_salt.astype("float")
noise_pepper.astype("float")
salt = peppers + noise_salt
pepper = peppers + noise_pepper
salt = np.where(salt > 255, 255, salt)
pepper = np.where(pepper < 0, 0, pepper)
cv2.imshow("salt", salt.astype("uint8"))
cv2.imwrite("salt.png", salt)
cv2.imshow("pepper", pepper.astype("uint8"))
cv2.imwrite("pepper.png", pepper)
cv2.waitKey()


