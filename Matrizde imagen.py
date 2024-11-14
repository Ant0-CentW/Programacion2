import matplotlib.pyplot as plt
import random
import numpy as np
from PIL import Image,ImageOps
plt.rcParams["image.cmap"]="gray"
im1=Image.open("Wall-e.jpg")
im1gr=ImageOps.grayscale(im1)
ar=np.array(im1gr)

plt.imshow(ar)
plt.show()

f=280
c=377
au=0
for i in range(f): # va recorriendo la primera  mitad de las de las columnas de la  fila
    for j in range(int(c/2)): #calcula el indice opuesto de la fila
        ind_op=c-1-j     # guarda el valor temporalmente de las filas
        au=ar[i][j]n     # intercambia el valor posicionado de (j,i)
        ar[i][j]=ar[i][ind_op]  
        ar[i][ind_op]=au   #coloca el valor guardado en au
  
  
plt.imshow(ar)
plt.show()