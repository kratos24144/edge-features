import numpy as np
from skimage.io import imread, imshow
from skimage.filters import prewitt_h,prewitt_v 
import matplotlib.pyplot as plt  

image = imread('puppy.jpeg',as_gray=True)

edges_prewitt_horizontal = prewitt_h(image)

edges_prewitt_vertical = prewitt_v(image)

imshow(edges_prewitt_vertical,cmap ='gray')

image = imread('puppy.jpeg')
feature_matrix = np.zeroes((660,450))
feature_matrix.shape

features = np.reshape(feature_matrix, (660*450))
features.shape

for i in range(0,image.shape[0]):
    for j in range(0,image.shape[1]):
        feature_matrix[i][j] = ((int(image[i,j,0]) + int(image[i,j,1]) + int(image[i,j,2]))/3)

image = imread('puppy.jpeg', as_gray=True) 
image.shape, imshow(image)

image = imread('puppy.jpeg') 
image.shape

image.shape, image

features = np.reshape(image, (660*450))

features.shape, features

