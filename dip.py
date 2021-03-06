from PIL import Image
import matplotlib.pylab as plt
import numpy as np
import torch

#Loads Image
imagePath = Image.open('C:\\Users\\ACER\\Desktop\\dip\\sample.png')
#Resizes Image
imgResize = imagePath.resize((300,300))

#Converts to numpy array
img = np.array(imgResize)

#Laplacian Filter
laplacianFilter = np.array([[0,1,0],[1,-4,1],[0,1,0]])

#Sobel Filter
sobelX = np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
sobelY = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])

#Prewitt Filter
prewittX =  np.array([[-1,-1,-1],[0,0,0],[1,1,1]])
prewittY = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])



#Image Zero Padding - Top and Sides
imgPadded = np.pad(img,((1,1),(1,1),(0,0)),'constant') 

#Assign height and width
h, w = imgPadded.shape[0], imgPadded.shape[1]

r, c = laplacianFilter.shape

def conv(mat1, mat2):
  val = np.dot(mat1, mat2)
  return np.sum(val)

def splitChannels(mat, filter):
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


#Main Function - Laplace Filter
def laplacian():
  filter = laplacianFilter
  ans = []
  for i in range(0, w-2):
      temp = []
      for j in range(0, h-2):
          mat = []
          for k in range(i, i+3):
              l = []
              for q in range(j, j+3):
                  l.append(imgPadded[k][q])
              mat.append(l)

          val = splitChannels(mat, filter)
          
          x = list(val)
          #print(i,j)
          temp.append(x)
      ans.append(temp)
  plt.imshow(ans)

#Main Function - Sobel Filter
def sobel(): 
  #Setting Filter
  filterX = sobelX
  filterY = sobelY
  ans = []
  for i in range(0, w-2):
      temp = []
      for j in range(0, h-2):
          mat = []
          for k in range(i, i+3):
              l = []
              for q in range(j, j+3):
                  l.append(imgPadded[k][q])
              mat.append(l)

          val1 = splitChannels(mat, filterX)
          val2 = splitChannels(mat, filterY)
          
          x = np.add(list(val1), list(val2))
          
          #print(i,j)
          temp.append(x)
      ans.append(temp)
  plt.imshow(ans)


#Main Function - Prewitt Filter
def prewitt(): 
  #Setting Filter
  filterX = prewittX
  filterY = prewittY
  ans = []
  for i in range(0, w-2):
      temp = []
      for j in range(0, h-2):
          mat = []
          for k in range(i, i+3):
              l = []
              for q in range(j, j+3):
                  l.append(imgPadded[k][q])
              mat.append(l)

          val1 = splitChannels(mat, filterX)
          val2 = splitChannels(mat, filterY)
          
          x = np.add(list(val1), list(val2))
          
          #print(i,j)
          temp.append(x)
      ans.append(temp)
  plt.imshow(ans)

plt.imshow(imgResize)

laplacian()
plt.imshow(ans)

sobel()

prewitt()