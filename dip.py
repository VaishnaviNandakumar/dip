# -*- coding: utf-8 -*-
"""DIP.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1h62d4r2gbtyJxdim7Vootoelo4icUUsX
"""

from PIL import Image
import matplotlib.pylab as plt
import numpy as np
import torch

im = Image.open('/content/sample.png')
im2 = im.resize((300,300))

img = np.array(im2)
img.shape

filter = np.array([[0,1,0],[1,-4,1],[0,1,0]])

plt.imshow(img)

img2=np.pad(img,((1,1),(1,1),(0,0)),'constant')

h, w = img2.shape[0], img2.shape[1]
h,w

img2.shape

res = img
res.shape

r, c = filter.shape

def conv(mat1, mat2):
  val = np.dot(mat1, mat2)
  return np.sum(val)

def splitChannels(mat):
  redChannel = []
  greenChannel = []
  blueChannel = []
  for i in range(3):
    l1 = []
    l2 = []
    l3 = []
    for j in range(3):
      r = mat[i][j][0]
      g = mat[i][j][1]
      b = mat[i][j][2]
      l1.append(r)
      l2.append(g)
      l3.append(b)
    redChannel.append(l1)
    greenChannel.append(l2)
    blueChannel.append(l3)
  #print(redChannel)
  #print(greenChannel)
  #print(blueChannel)
  x = conv(redChannel, filter)
  y = conv(greenChannel, filter)
  z = conv(blueChannel, filter)
  return x, y, z

ans = []
for i in range(0, w-2):
    temp = []
    for j in range(0, h-2):
        mat = []
        

        for k in range(i, i+3):
            l = []
            for q in range(j, j+3):
                l.append(img2[k][q])
            mat.append(l)

        val = splitChannels(mat)
        
        x = list(val)
        #print(i,j)
        temp.append(x)
    ans.append(temp)

ans = np.array(ans)
ans.shape

y = ans * 4

plt.imshow(y)