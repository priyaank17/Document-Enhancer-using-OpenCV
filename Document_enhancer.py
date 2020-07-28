#!/usr/bin/env python
# coding: utf-8

# In[3]:


import cv2
import numpy as np
import imageio
import argparse





img=cv2.imread('DSC_2113 2.jpg',0)


#img = cv2.imread(file,0)
img = cv2.medianBlur(img,5)

ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,            cv2.THRESH_BINARY,11,2)
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,            cv2.THRESH_BINARY,11,2)

titles = ['Original_Image', 'Global_Thresholding (v = 127)',
            'Adaptive_Mean_Thresholding', 'Adaptive_Gaussian Thresholding']
images = [img, th1, th2, th3]

gif_images=[]
for i in range(0,4):
    cv2.namedWindow(titles[i],cv2.WINDOW_NORMAL)
    cv2.imshow(titles[i], images[i])
    #cv2.imwrite(filename+"_"+titles[i]+".jpg",images[i])
    #gif_images.append(imageio.imread(filename+"_"+titles[i]+".jpg"))
    cv2.waitKey(0)


# In[ ]:




