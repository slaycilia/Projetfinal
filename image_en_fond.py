import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

# Création du plot
fig, ax = plt.subplots()

# Chargement de l'image
image = plt.imread('testimage.jpg')
xmin=0
ymin=0
xmax=710.33
ymax=673.15
"""Le repere local est oriente vers 33° Est"""
# Affichage de l'image de fond
ax.imshow(image,extent=[xmin, xmax, ymin, ymax], aspect='auto',alpha=0.5)

# Tracer vos données sur le plot
# ...

# Affichage du plot
plt.show()
