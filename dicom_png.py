import pydicom as dicom
import os
#import cv2
import types
import numpy as np
from scipy.misc import imsave
import matplotlib.pyplot as plt
import mritopng

#mritopng.convert_folder('C:/Users/twistcode/Documents/bc/mammo/all', 'C:/Users/twistcode/Documents/bc/mammo_png')

from PIL import Image
import glob

for name in glob.glob('C:/Users/twistcode/Documents/bc/mias_mammo/all/*.pgm'):
    im = Image.open(name)
    name = str(name).rstrip(".pgm")
    im.save(name + '.jpg', 'JPEG')

print("Conversion from pgm to jpg completed!")



'''
# specify your image path
image_path = 'cancer.dcm'
ds = dicom.dcmread(image_path)

#plt.imshow( ds.pixel_array)
#plt.show()

'''

'''
folder_path = "Lung_cancer_dicom"
jpg_folder_path = "Lung_dicom_jpg"
images_path = os.listdir(folder_path)

for image in enumerate(images_path):
    img = dicom.dcmread(os.path.join(folder_path, image))
    img = dicom.dcmread(os.path.join(folder_path, image))
    pixel_array_numpy = img.pixel_array
    #img = dicom.dcmread('cancer.dcm')
    img=np.stack([img] * 3, axis=2)
    imsave(os.path.join(jpg_folder_path, image), pixel_array_numpy)

'''


'''
import PIL # optional
# make it True if you want in PNG format
PNG = False
# Specify the .dcm folder path
folder_path = "Lung_png/normal"
# Specify the output jpg/png folder path
jpg_folder_path = "Lung_png/normal"
images_path = os.listdir(folder_path)
for n, image in enumerate(images_path):
    ds = dicom.dcmread(os.path.join(folder_path, image))
    pixel_array_numpy = ds.pixel_array
    if PNG == False:
        image = image.replace('.dcm', '.jpg')
    else:
        image = image.replace('.dcm', '.png')
    cv2.imwrite(os.path.join(jpg_folder_path, image), pixel_array_numpy)
    if n % 50 == 0:
        print('{} image converted'.format(n))

'''

