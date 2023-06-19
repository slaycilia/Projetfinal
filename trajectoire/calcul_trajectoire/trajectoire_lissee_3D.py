import math
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

class TrajectoireDrone3D:
    def __init__(self, points_passage, resolution):
        self.points_passage = points_passage
        self.resolution = resolution
        self.trajectoire_3D = self.calculer_trajectoire_3D()

    def calculer_distance(self, point1, point2):
        # Calcule la distance entre deux points en utilisant le théorème de Pythagore.
        dx = point2[0] - point1[0]
        dy = point2[1] - point1[1]
        dz = point2[2] - point1[2]
        distance = math.sqrt(dx ** 2 + dy ** 2 + dz ** 2)
        return distance

    def calculer_angle(self, point1, point2):
        # Calcule l'angle entre deux points par rapport à l'axe x positif.
        dx = point2[0] - point1[0]
        dy = point2[1] - point1[1]
        dz = point2[2] - point1[2]
        angle = math.atan2(dy, dx)
        return angle

    def calculer_points_intermediaires(self, point1, point2):
        # Calcule les points intermédiaires entre deux points en fonction d'une résolution donnée.
        distance = self.calculer_distance(point1, point2)
        angle = self.calculer_angle(point1, point2)
        pas = distance / (self.resolution + 1)
        points_intermediaires = []
        for i in range(1, self.resolution + 1):
            x = point1[0] + i * pas * math.cos(angle)
            y = point1[1] + i * pas * math.sin(angle)
            z = point1[2] + i * pas * math.sin(angle)
            points_intermediaires.append((x, y, z))
        return points_intermediaires

    def fonction_polynomiale(self, x, a, b, c, d):
        # Fonction polynomiale utilisée pour l'ajustement de courbe.
        return a * x ** 3 + b * x ** 2 + c * x + d

    def calculer_trajectoire_3D(self):
        # Calcule la trajectoire du drone en utilisant une liste de waypoints (points clés de repère).
        trajectoire = []
        for i in range(len(self.points_passage) - 1):
            point_actuel = self.points_passage[i]
            point_suivant = self.points_passage[i + 1]
            points_intermediaires = self.calculer_points_intermediaires(point_actuel, point_suivant)
            trajectoire.extend(points_intermediaires)
        trajectoire.append(self.points_passage[-1])  # Ajouter le dernier waypoint à la trajectoire
        return trajectoire

# Utilisation de la classe

waypoints = [(0, 0, 10),
             (100, 100, 20),
             (200, 200, 30),
             (300, 300, 40),
             (400, 400, 10),
             (500, 500, 20),
             (600, 600, 30),
             (700, 600, 40),
             (800, 500, 10),
             (900, 400, 20)]

resolution = 100  # Ajustez la résolution selon vos besoins
trajectoire = TrajectoireDrone3D(waypoints, resolution).trajectoire_3D

# Extraction des coordonnées x, y et z de la trajectoire
x_coords = np.array([point[0] for point in trajectoire])
y_coords = np.array([point[1] for point in trajectoire])
z_coords = np.array([point[2] for point in trajectoire])

# Ajustement de courbe
initial_guess = [1, 1, 1, 1]  # Estimation initiale des coefficients
coeffs, _ = curve_fit(TrajectoireDrone3D().fonction_polynomiale, x_coords, y_coords, p0=initial_guess)
coeffs1, _ = curve_fit(TrajectoireDrone3D().fonction_polynomiale, x_coords, z_coords, p0=initial_guess)
coeffs2, _ = curve_fit(TrajectoireDrone3D().fonction_polynomiale, y_coords, x_coords, p0=initial_guess)

# Génération de la trajectoire ajustée
x_interp = np.linspace(min(x_coords), max(x_coords), resolution)
y_interp = TrajectoireDrone3D().fonction_polynomiale(x_interp, *coeffs)
z_interp = TrajectoireDrone3D().fonction_polynomiale(x_interp, *coeffs1)
x_interp = TrajectoireDrone3D().fonction_polynomiale(y_interp, *coeffs2)

# Tracé de la trajectoire
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x_interp, y_interp, z_interp, marker='o')
ax.plot(x_coords, y_coords, z_coords)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Trajectoire du drone (Lissée avec curve_fit)')
plt.show()
