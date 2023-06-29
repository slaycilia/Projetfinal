import math
import numpy as np

class TrajectoireDrone2D:
    def __init__(self, points_passage, resolution):
        self.points_passage = points_passage
        self.resolution = resolution

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


        s_arg = np.linspace(0, 1, len(trajectoire))  # Nouvel array s_arg

        coeffs = np.polyfit(s_arg, x_coords, 30)
        coeffs2=np.polyfit(s_arg, y_coords, 30)


        x_interp = np.polyval(coeffs, s_arg)
        y_interp = np.polyval(coeffs2, s_arg)

        trajectoire_lissee = [(x, y) for x, y in zip(x_interp, y_interp)]

        return trajectoire_lissee