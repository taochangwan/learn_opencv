# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 18:04:55 2018

@author: 天津拨云咨询服务有限公司  

@author: 李立宗  lilizong@gmail.com
《opencv图穷匕见-python实现》 电子工业出版社
"""



import matplotlib.pyplot as plt
img = cv2.imread('image\\lena.bmp',0)
dft = cv2.dft(np.float32(img),flags = cv2.DFT_COMPLEX_OUTPUT)
dftShift = np.fft.fftshift(dft)
result = 20*np.log(cv2.magnitude(dftShift[:,:,0],dftShift[:,:,1]))
plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('original'),plt.axis('off')
plt.subplot(122),plt.imshow(result, cmap = 'gray')
plt.title('result'), plt.axis('off')
plt.show()
#print(dft)