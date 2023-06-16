import math
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt


def calculer_distance(point1, point2):
    """
    Calcule la distance entre deux points en utilisant le théorème de Pythagore.
    Chaque point est une paire de coordonnées (x, y).
    """
    dx = point2[0] - point1[0]
    dy = point2[1] - point1[1]
    distance = math.sqrt(dx**2 + dy**2)
    return distance

def calculer_angle(point1, point2):
    """
    Calcule l'angle entre deux points par rapport à l'axe x positif.
    Chaque point est une paire de coordonnées (x, y).
    L'angle est retourné en radians.
    """
    dx = point2[0] - point1[0]
    dy = point2[1] - point1[1]
    angle = math.atan2(dy, dx)
    return angle
def polynomial_func(x, a, b, c, d):
    """
    Fonction polynomiale utilisée pour l'ajustement de courbe.
    x : variable indépendante
    a, b, c, d : coefficients du polynôme
    """
    return a * x**3 + b * x**2 + c * x + d


def calculer_points_intermediaires(point1, point2, resolution):
    """
    Calcule les points intermédiaires entre deux points en fonction d'une résolution donnée.
    Chaque point est une paire de coordonnées (x, y).
    La résolution détermine le nombre de points intermédiaires à générer.
    """
    distance = calculer_distance(point1, point2)
    angle = calculer_angle(point1, point2)
    pas = distance / (resolution + 1)
    points_intermediaires = []
    for i in range(1, resolution + 1):
        x = point1[0] + i * pas * math.cos(angle)
        y = point1[1] + i * pas * math.sin(angle)
        points_intermediaires.append((x, y))
    return points_intermediaires

def calculer_trajectoire(waypoints, resolution):
    """
    Calcule la trajectoire du drone en utilisant une liste de waypoints (points clés de repère).
    Chaque waypoint est une paire de coordonnées (x, y).
    La trajectoire est une liste de points (x, y) formant une séquence de déplacements linéaires.
    La résolution détermine le nombre de points intermédiaires à générer entre chaque paire de waypoints.
    """
    trajectoire = []
    for i in range(len(waypoints)-1):
        point_actuel = waypoints[i]
        point_suivant = waypoints[i+1]
        points_intermediaires = calculer_points_intermediaires(point_actuel, point_suivant, resolution)
        trajectoire.extend(points_intermediaires)
    trajectoire.append(waypoints[-1])  # Ajouter le dernier waypoint à la trajectoire
    return trajectoire

waypoints = [(0, 0), (5, 3), (8, 2), (10, 5)]
resolution = 100  # Ajustez la résolution selon vos besoins
trajectoire = calculer_trajectoire(waypoints, resolution)


# Extraction des coordonnées x et y de la trajectoire
x_coords = np.array([point[0] for point in trajectoire])
y_coords = np.array([point[1] for point in trajectoire])

# Ajustement de courbe
initial_guess = [100, 100, 100, 100]  # Estimation initiale des coefficients
coeffs, _ = curve_fit(polynomial_func, x_coords, y_coords, p0=initial_guess)

#Trajectoire brute


# Génération de la trajectoire ajustée
x_interp = np.linspace(min(x_coords), max(x_coords), resolution)
y_interp = polynomial_func(x_interp, *coeffs)

# Tracé de la trajectoire
plt.plot(x_interp, y_interp, marker='o')
plt.plot(x_coords,y_coords)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Trajectoire du drone (Lissée avec curve_fit)')
plt.grid(True)
plt.show()