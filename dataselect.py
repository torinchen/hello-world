# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 16:22:53 2017
matlab data collecting
@author: Torin
"""
import numpy as np
import scipy.io as sio 
root_dir='C:/Users/Torin/Desktop/spyder/matlabdata/'
filename='Channel1time_vs_LambdaShift.txt'
#data=sio.loadmat(root_dir+filename)  
data=np.loadtxt(root_dir+filename,delimiter='  ,  ', dtype=str)
data2=data[:,1]
data3=np.array([float(x) for x in data2])
Raw_time=data[:,0]
time=[]
for i in range(0,len(data2)):
     a=Raw_time[i].split(':')
     time.append(float(a[0])*3600+float(a[1])*60+float(a[2]))
time_array=np.array(time)
