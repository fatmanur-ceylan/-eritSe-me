import cv2
from matplotlib import pyplot as plt
import numpy as np

img=cv2.imread("yol.jpg")

#once yoldaki beyaz seyleri gosterdik
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

(thresh,output2)=cv2.threshold(gray_img,220,255,cv2.THRESH_BINARY)
output2=cv2.GaussianBlur(output2,(5,5),3)
output2=cv2.Canny(output2,180,255)
cv2.imshow("2",output2)

#maske olusturma
mask=np.zeros_like(output2)
vertices=np.array([[(100,500),(200,350),(520,250),(920,525)]],np.int32)
cv2.fillPoly(mask,vertices,255)
plt.imshow(mask,cmap="gray")
plt.show()

#maske ile resmi birlestirdik
masked=cv2.bitwise_and(output2,mask)
plt.imshow(masked,cmap="gray")
plt.show()
lines=cv2.HoughLinesP(masked,1,np.pi/180,30)

#bunu yola uyguladik
for line in lines:
    x1,y1,x2,y2=line[0]
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),4)
cv2.imshow("son_img",img)
#once yoldaki beyaz seyleri gosterdik
#ona gore make olusturduk
#maske ile resmi birlestirdik
#bunu yola uyguladik

