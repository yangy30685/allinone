import cv2
import numpy as np
 
path = 'C:\\Users\\yangy\\Documents\\GitHub\\allinone\\python\\image_improve\\metastable.PNG'

im = cv2.imread(path)
im = im/255.0
im_power_law_transformation = cv2.pow(im,3) # change the value 1.5 for change

cv2.imshow('Original Image',im)
cv2.imshow('Power Law Transformation',im_power_law_transformation)
cv2.waitKey(0)

