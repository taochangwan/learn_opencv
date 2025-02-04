# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 08:16:09 2018

@author: 天津拨云咨询服务有限公司  lilizong@gmail.com
"""

def saltpepper(img,n):
    m=int((img.shape[0]*img.shape[1])*n)
    for a in range(m):
        i=int(np.random.random()*img.shape[1])
        j=int(np.random.random()*img.shape[0])
        if img.ndim==2:
            img[j,i]=255
        elif img.ndim==3:
            img[j,i,0]=255
            img[j,i,1]=255
            img[j,i,2]=255
    for b in range(m):
        i=int(np.random.random()*img.shape[1])
        j=int(np.random.random()*img.shape[0])
        if img.ndim==2:
            img[j,i]=0
        elif img.ndim==3:
            img[j,i,0]=0
            img[j,i,1]=0
            img[j,i,2]=0
    return img


#上面就是椒盐噪声函数，下面是使用方法，大家可以愉快的玩耍了
img=cv2.imread('image\\lena.bmp')
saltImage=saltpepper(img,0.02)
cv2.imshow('saltImage',saltImage)

cv2.imwrite('image\\test.jpg',img)

cv2.waitKey(0)
cv2.destroyAllWindows()