import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2

img=mpimg.imread('normal_17.png')
imgplot = plt.imshow(img)
#plt.show()

ret, thresh = cv2.threshold(img,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)





