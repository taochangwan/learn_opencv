# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 10:18:42 2018

@author: 李立宗  lilizong@gmail.com
《OpenCV图穷匕见——Python实现》 电子工业出版社
"""

lena=cv2.imread("lena.bmp")
cv2.imshow("demo", lena )
key=cv2.waitKey()
if key==ord('a'):
    cv2.imshow("PressA",lena)
elif key==ord('b'):
    cv2.imshow("PressB",lena)



