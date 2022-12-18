import numpy as np
import cv2

img = cv2.imread("isim.png",0)
cv2.imshow("Original",img)
cv2.waitKey(0)

kernel = np.ones((5,5),dtype=np.uint8)

result = cv2.dilate(img,kernel,iterations=1)
cv2.imshow("Dilation",result)
cv2.waitKey(0)