import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

class TrajectoireDrone2D:
    def __init__(self, points_passage, resolution, xmin, ymin, xmax, ymax):
        self.points_passage = points_passage
        self.resolution = resolution
        self.xmin = xmin
        self.ymin = ymin
        self.xmax = xmax
        self.ymax = ymax

    def calculer_distance(self, point1, point2):
        dx = point2[0] - point1[0]
        dy = point2[1] - point1[1]
        distance = math.sqrt(dx ** 2 + dy ** 2)
        return distance

    def calculer_angle(self, point1, point2):
        dx = point2[0] - point1[0]
        dy = point2[1] - point1[1]
        angle = math.atan2(dy, dx)
        return angle

    def calculer_points_intermediaires(self, point1, point2):
        distance = self.calculer_distance(point1, point2)
        angle = self.calculer_angle(point1, point2)
        pas = distance / (self.resolution + 1)
        points_intermediaires = []
        for i in range(1, self.resolution + 1):
            x = point1[0] + i * pas * math.cos(angle)
            y = point1[1] + i * pas * math.sin(angle)
            points_intermediaires.append((x, y))
        return points_intermediaires

    def calculer_trajectoire(self):
        trajectoire = []
        for i in range(len(self.points_passage) - 1):
            point_actuel = self.points_passage[i]
            point_suivant = self.points_passage[i + 1]
            points_intermediaires = self.calculer_points_intermediaires(point_actuel, point_suivant)
            trajectoire.extend(points_intermediaires)
        trajectoire.append(self.points_passage[-1])
        return trajectoire

    def fonction_polynomiale(self, x, a, b, c, d):
        return a * x ** 3 + b * x ** 2 + c * x + d

    def lisser_trajectoire(self):
        trajectoire = self.calculer_trajectoire()
        x_coords = np.array([point[0] for point in trajectoire])
        y_coords = np.array([point[1] for point in trajectoire])

        initial_guess = [100, 100, 100, 100]
        coeffs, _ = curve_fit(self.fonction_polynomiale, x_coords, y_coords, p0=initial_guess)

        x_interp = np.linspace(min(x_coords), max(x_coords), self.resolution)
        y_interp = self.fonction_polynomiale(x_interp, *coeffs)

        return x_interp, y_interp

    def tracer_trajectoire_2D(self):
        image = plt.imread('/Users/ceciliou/Document/ETS MTL/MGA802_ETE/Projetfinal/Projet/Sans titre/trajectoire/graphique/testimage.jpg')
        fig, ax = plt.subplots()
        ax.imshow(image, extent=[self.xmin, self.xmax, self.ymin, self.ymax], aspect='auto', alpha=0.5)
        x_interp, y_interp = self.lisser_trajectoire()
        plt.plot(x_interp, y_interp, marker='o', label='Trajectoire lissée')

        trajectoire = self.calculer_trajectoire()
        x_coords = [point[0] for point in trajectoire]
        y_coords = [point[1] for point in trajectoire]
        plt.plot(x_coords, y_coords, marker='o', label='Trajectoire initiale')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Trajectoire du drone')
        plt.grid(True)
        plt.legend()
        plt.show()


