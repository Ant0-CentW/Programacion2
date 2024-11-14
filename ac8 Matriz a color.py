import matplotlib.pyplot as plt
import numpy as np
from PIL import Image,ImageOps
plt.rcParams["image.cmap"] = 'gray'

im1=Image.open("Wall-e.jpg")
ar=np.array(im1)

plt.imshow(ar)
plt.show()

f=50
c=50

m=np.zeros((50,50))
plt.imshow(m)
plt.show()


for i in range(f):
    for j in range (c):
        M[i][j]=ar[i][j][0]*0.2989+ar[i][j][1]*0.5870+ar[i][j][2]*0.1140       
        
plt.imshow(m)
plt.show()