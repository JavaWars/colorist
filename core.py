import cv2
import numpy as np

print("opening source image")
img = cv2.imread("colorist.png")

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#detecting upper and low range
up_range = np.array([255,255,255])
low_range = np.array([0,1,1])

#detecting intersection with range
mask = cv2.inRange(hsv, low_range, up_range)

cv2.imshow("image", img)
cv2.imshow("Byte Mask for searching color", mask)

print("PROGRAMM FINISHED, please CLOSE IT")
cv2.waitKey(0)
cv2.destroyAllWindows()

