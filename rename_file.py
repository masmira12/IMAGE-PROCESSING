import os
import pandas as pd


os.chdir('D:/bc/LUNG/TB/Cmpr/tb/')
i=1
for file in os.listdir():
    src=file
    dst="tb_"+ str(i)+".png"
    #dst=str(i) + "cancer" + ".jpg"
    os.rename(src,dst)
    i+=1

'''
labels = pd.read_csv('C:/Users/twistcode/Documents/bc/tb/tb_data1/tb')
i=1

for name in labels['image_id']:
    src=name
    dst="tb_1"+ str(i)+".png"
    #dst=str(i) + "cancer" + ".jpg"
    os.rename(src,dst)
    i+=1

'''


