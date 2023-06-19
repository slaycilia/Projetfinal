import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def tracer_sphere(ax, centre, rayon, resolution=20, couleur='b'):
    """
    Trace une sphère sur un graphique 3D.
    ax : Axes3D, le graphique 3D existant où tracer la sphère.
    centre : tuple (x, y, z), les coordonnées du centre de la sphère.
    rayon : float, le rayon de la sphère.
    resolution : int, la résolution de la sphère (le nombre de points à utiliser pour la discrétisation).
    couleur : str, la couleur de la sphère (par défaut 'b' pour bleu).
    """
    u = np.linspace(0, 2 * np.pi, resolution)
    v = np.linspace(0, np.pi, resolution)
    x = rayon * np.outer(np.cos(u), np.sin(v)) + centre[0]
    y = rayon * np.outer(np.sin(u), np.sin(v)) + centre[1]
    z = rayon * np.outer(np.ones(np.size(u)), np.cos(v)) + centre[2]
    ax.plot_surface(x, y, z, color=couleur)

def tracer_cube(ax, centre, cote, couleur='r'):
    """
    Trace un cube sur un graphique 3D.
    ax : Axes3D, le graphique 3D existant où tracer le cube.
    centre : tuple (x, y, z), les coordonnées du centre du cube.
    cote : float, la longueur du côté du cube.
    couleur : str, la couleur du cube (par défaut 'r' pour rouge).
    """
    demi_cote = cote / 2
    x = np.array([-demi_cote, demi_cote, demi_cote, -demi_cote, -demi_cote, demi_cote, demi_cote, -demi_cote])
    y = np.array([-demi_cote, -demi_cote, demi_cote, demi_cote, -demi_cote, -demi_cote, demi_cote, demi_cote])
    z = np.array([-demi_cote, -demi_cote, -demi_cote, -demi_cote, demi_cote, demi_cote, demi_cote, demi_cote])
    x += centre[0]
    y += centre[1]
    z += centre[2]
    ax.plot(x[[0, 1]], y[[0, 1]], z[[0, 1]], color=couleur)
    ax.plot(x[[1, 2]], y[[1, 2]], z[[1, 2]], color=couleur)
    ax.plot(x[[2, 3]], y[[2, 3]], z[[2, 3]], color=couleur)
    ax.plot(x[[3, 0]], y[[3, 0]], z[[3, 0]], color=couleur)
    ax.plot(x[[4, 5]], y[[4, 5]], z[[4, 5]], color=couleur)
    ax.plot(x[[5, 6]], y[[5, 6]], z[[5, 6]], color=couleur)
    ax.plot(x[[6, 7]], y[[6, 7]], z[[6, 7]], color=couleur)
    ax.plot(x[[7, 4]], y[[7, 4]], z[[7, 4]], color=couleur)
    ax.plot(x[[0, 4]], y[[0, 4]], z[[0, 4]], color=couleur)
    ax.plot(x[[1, 5]], y[[1, 5]], z[[1, 5]], color=couleur)
    ax.plot(x[[2, 6]], y[[2, 6]], z[[2, 6]], color=couleur)
    ax.plot(x[[3, 7]], y[[3, 7]], z[[3, 7]], color=couleur)

# Exemple d'utilisation

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Traçage d'une sphère
centre_sphere = (0, 0, 0)
rayon_sphere = 1.5
tracer_sphere(ax, centre_sphere, rayon_sphere, couleur='b')

# Traçage d'un cube
centre_cube = (2, 2, 2)
cote_cube = 2.0
tracer_cube(ax, centre_cube, cote_cube, couleur='r')

# Paramètres de l'affichage
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Sphère et cube en 3D')

plt.show()