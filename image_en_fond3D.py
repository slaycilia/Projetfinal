import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from PIL import Image

image_jpg = Image.open('testimage.jpg')
image_png_path ='testimage.png'
image_jpg.save(image_png_path,'PNG')
# Création du plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Chargement de l'image
image = plt.imread('testimage.png')
xmin=0
ymin=0
xmax=710.33
ymax=673.15
zmax=200
"""Le repere local est oriente vers 33° Est"""
x = np.linspace(xmin, xmax, image.shape[1])
y = np.linspace(ymin, ymax, image.shape[0])
X, Y = np.meshgrid(x, y)
# Affichage de l'image de fond
ax.plot_surface(X, Y, np.zeros_like(X), facecolors=image)

# Tracer vos données sur le plot
# ...
plt.xlim(xmin,xmax)
plt.ylim(ymin,ymax)
ax.set_zlim(0, zmax)
# Affichage du plot
plt.show()
