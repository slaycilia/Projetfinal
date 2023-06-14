import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

# Création du plot
fig, ax = plt.subplots()

# Chargement de l'image
image = plt.imread('testlafontaine.png')

# Affichage de l'image de fond
ax.imshow(image, aspect='auto')

# Tracer vos données sur le plot
# ...

# Affichage du plot
plt.show()
