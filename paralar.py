#Canny algoritmasýnýn daha çok iþe yaramasý için öncesinde blurlastýrmasý yapýlýr

import cv2
import matplotlib.pyplot as plt
import numpy as np

img=cv2.imread("paralar.jpeg")

gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

(thresh,output2)=cv2.threshold(gray_img,120,255,cv2.THRESH_BINARY) #hangi deger uygunsa denemen gerekiyor 120 icin ,255 de olabilir

cv2.imshow("Esikleme",output2)

output2=cv2.GaussianBlur(output2,(5,5),1)

output2=cv2.Canny(output2,180,255)

plt.imshow(output2,cmap=plt.get_cmap("gray"))

circles=cv2.HoughCircles(output2,cv2.HOUGH_GRADIENT,1,10,
                         param1=180,param2=27,minRadius=20,maxRadius=60)

circles=np.uint16(np.around(circles))

for i in circles[0,:]:
    cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
    cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)

cv2.imshow("img",img)
