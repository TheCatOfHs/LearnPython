# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 20:02:37 2017

@author: vento
"""

import os, math
from skimage import io
import numpy as np

N = 2500

def readPicture(files):
    Picture = np.zeros([len(files), N+1])
    for i, item in enumerate(files):
        img = io.imread('./num/'+item, as_grey = True).reshape(N)
        Picture[i, 0:N] = img
        Picture[i, N] = float(item[0])
    return Picture

def readTestPicture(files):
    Picture = np.zeros([len(files), N])
    for i, item in enumerate(files):
        img = io.imread(item, as_grey = True).reshape(N)
        Picture[i, 0:N] = img
    return Picture

def calDis(pic, testPic):
    dis = np.zeros([2, len(pic)])
    for i, item in enumerate(pic):
        Item = item[0:N]
        dis[0, i] = np.sqrt(abs(np.sum(Item**2-testPic**2)))
        dis[1, i] = item[N]
    return dis

def chooseClass(dis):
    disMin = np.min(dis[0,:])
    point = list(dis[0,:]).index(disMin)
    return dis[1, point]

filenames = os.listdir(r"./num/")
pic = readPicture(filenames)
testPic = readTestPicture(['test.png'])
distance = calDis(pic, testPic)
picClass = chooseClass(distance)
print('这个数是', picClass)