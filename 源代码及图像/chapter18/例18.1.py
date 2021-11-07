# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 10:08:27 2018

@author: 李立宗  lilizong@gmail.com
《opencv图穷匕见-python实现》 电子工业出版社
"""



cap = cv2.VideoCapture(0)
while(cap.isOpened()):
    ret, frame = cap.read()
    cv2.imshow('frame',frame)
    c = cv2.waitKey(1)
    if c==27:   #ESC键
        break
cap.release()
cv2.destroyAllWindows()