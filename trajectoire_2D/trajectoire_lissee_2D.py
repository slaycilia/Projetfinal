import math

class TrajectoireDrone2D :
    def __init__(self,points_passage,resolution):
        self.points_passage = points_passage   # Points indiqués par l'utilisateur par lesquels le drône doit dans l'idéal passer
        self. resolution = resolution # Résolution de la trajectoire lissée idéale tracée
        self.trajectoire_2D = self.calculer_trajectoire_2D_lisse

    def calculer_distance(self, point1, point2):
        """
            Calcule la distance entre deux points en utilisant le théorème de Pythagore.
            Chaque point est une paire de coordonnées (x, y).
            """
        dx = point2[0] - point1[0]
        dy = point2[1] - point1[1]
        distance = math.sqrt(dx ** 2 + dy ** 2)
        return distance

    def calculer_angle(self, point1, point2):
        """
            Calcule l'angle entre deux points par rapport à l'axe x positif.
            Chaque point est une paire de coordonnées (x, y).
            L'angle est retourné en radians.
            """
        dx = point2[0] - point1[0]
        dy = point2[1] - point1[1]
        angle = math.atan2(dy, dx)
        return angle

    def fonction_polynomiale(self, x, a, b, c, d):
        """
            Fonction polynomiale utilisée pour l'ajustement de courbe.
            x : variable indépendante
            a, b, c, d : coefficients du polynôme
            """
        return a * x ** 3 + b * x ** 2 + c * x + d

    def calculer_points_intermediaires(self, point1, point2):
        """
            Calcule les points intermédiaires entre deux points en fonction d'une résolution donnée.
            Chaque point est une paire de coordonnées (x, y).
            La résolution détermine le nombre de points intermédiaires à générer.
            """
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
        """
           Calcule la trajectoire du drone en utilisant une liste de waypoints (points clés de repère).
           Chaque waypoint est une paire de coordonnées (x, y).
           La trajectoire est une liste de points (x, y) formant une séquence de déplacements linéaires.
           La résolution détermine le nombre de points intermédiaires à générer entre chaque paire de waypoints.
           """
        trajectoire = []
        for i in range(len(self.points_passage) - 1):
            point_actuel = self.points_passage[i]
            point_suivant = self.points_passage[i + 1]
            points_intermediaires = self.calculer_points_intermediaires(point_actuel, point_suivant)
            trajectoire.extend(points_intermediaires)
        trajectoire.append(self.points_passage[-1])
        return trajectoire

    def lisser_trajectoire(self):
        x_coords = np.array([point[0] for point in self.trajectoire])
        y_coords = np.array([point[1] for point in self.trajectoire])

        initial_guess = [100, 100, 100, 100]
        coeffs, _ = curve_fit(self.fonction_polynomiale(), x_coords, y_coords, p0=initial_guess)

        x_interp = np.linspace(min(x_coords), max(x_coords), self.resolution)
        y_interp = self.polynomial_func(x_interp, *coeffs)

        return x_interp, y_interp

    def tracer_trajectoire_2D(self):
        x_interp, y_interp = self.ajuster_trajectoire()
        plt.plot(x_interp, y_interp, marker='o')
        plt.plot(*zip(*self.trajectoire), marker='o')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Trajectoire du drone (Lissée avec curve_fit)')
        plt.grid(True)
        plt.show()