import math
import numpy as np

class TrajectoiresDeriveeEtInitiale:
    def __init__(self, trajectoire, vitesse_vent, angle_vent, surface_contact, force_drone):
        """
               Classe pour calculer la trajectoire dérivée et initiale d'un drone en fonction du vent.

               :param trajectoire: Liste de coordonnées de la trajectoire du drone.
               :type trajectoire: list[(float, float)]
               :param vitesse_vent: Vitesse du vent en m/s.
               :type vitesse_vent: float
               :param angle_vent: Direction du vent en degrés (0° correspondant au nord, angle positif dans le sens horaire).
               :type angle_vent: float
               :param surface_contact: Surface du drone en contact avec le vent en m².
               :type surface_contact: float
               :param force_drone: Force de traînée du drone en N.
               :type force_drone: float
               """
        self.trajectoire = trajectoire
        self.vitesse_vent = vitesse_vent
        self.angle_vent = angle_vent
        self.surface_contact = surface_contact
        self.force_drone = force_drone

    def calculer_vecteur_directeur(self, norme, angle_deg):
        """
               Calcule le vecteur directeur à partir d'une norme et d'un angle en degrés.

               :param norme: La norme du vecteur.
               :type norme: float
               :param angle_deg: L'angle en degrés.
               :type angle_deg: float
               :return: Le vecteur directeur (x, y).
               :rtype: tuple(float, float)
               """
        # Convertir l'angle de degrés à radians
        angle_rad = math.radians(angle_deg)
        # Calculer les composantes x et y du vecteur
        x = norme * np.cos(angle_rad)
        y = norme * np.sin(angle_rad)
        # Retourner le vecteur directeur (x, y)
        return (x, y)

    def calculer_vecteur_resultant(self, vecteur1, vecteur2):
        """
               Calcule le vecteur résultant de la somme de deux vecteurs.

               :param vecteur1: Le premier vecteur (x1, y1).
               :type vecteur1: tuple(float, float)
               :param vecteur2: Le deuxième vecteur (x2, y2).
               :type vecteur2: tuple(float, float)
               :return: Le vecteur résultant (x, y).
               :rtype: tuple(float, float)
               """
        # Calculer les composantes x et y du vecteur résultant
        x = vecteur2[0] + vecteur1[0]
        y = vecteur2[1] + vecteur1[1]
        # Retourner le vecteur résultant (x, y)
        return (x, y)

    def deplacer_point(self, point, vecteur):
        """
                Déplace un point en fonction d'un vecteur.

                :param point: Le point à déplacer (x, y).
                :type point: tuple(float, float)
                :param vecteur: Le vecteur de déplacement (dx, dy).
                :type vecteur: tuple(float, float)
                :return: La nouvelle position du point déplacé (x', y').
                :rtype: tuple(float, float)
                """
        # Décomposer les coordonnées du point
        x, y = point
        # Décomposer les composantes x et y du vecteur
        dx, dy = vecteur
        # Calculer la nouvelle position du point déplacé
        nouvelle_position = (x + dx, y + dy)
        # Retourner la nouvelle position du point déplacé
        return nouvelle_position

    def caluler_force_vent(self):
        """
               Calcule la force exercée par le vent sur le drone.

               :return: La force du vent en N.
               :rtype: float
               """
        densite_air = 1.2
        force_vent = 0.5 * densite_air * self.vitesse_vent ** 2 * self.surface_contact
        return force_vent

    def calculer_angle(self, x1, y1, x2, y2):
        """
                Calcule l'angle entre deux points.

                :param x1: Coordonnée x du premier point.
                :type x1: float
                :param y1: Coordonnée y du premier point.
                :type y1: float
                :param x2: Coordonnée x du deuxième point.
                :type x2: float
                :param y2: Coordonnée y du deuxième point.
                :type y2: float
                :return: L'angle en degrés entre les deux points.
                :rtype: float
                """
        # Calcul des différences entre les coordonnées
        delta_y = y2 - y1
        delta_x = x2 - x1
        # Calcul de la pente de la droite
        m = delta_y / delta_x
        # Calcul de l'angle en radians
        angle_rad = math.atan(m)
        # Conversion de l'angle en degrés
        angle_deg = math.degrees(angle_rad)
        return angle_deg

    def calculer_trajectoire_derivee(self):
        """
        Calcule la trajectoire dérivée du drone en fonction du vent.

        :return: La trajectoire dérivée du drone.
        :rtype: list[(float, float)]
        """
        # Initialisation de la trajectoire dérivée
        trajectoire_derivee = [self.trajectoire[0]]
        # Parcours de la trajectoire
        for i in range(1, len(self.trajectoire)):
            # Ajout du point dérivé à la trajectoire dérivée
            vecteur = self.calculer_vecteur_resultant(self.calculer_vecteur_directeur(self.force_drone, self.calculer_angle(self.trajectoire[i - 1][0], self.trajectoire[i - 1][1], self.trajectoire[i][0], self.trajectoire[i][1])), self.calculer_vecteur_directeur(self.caluler_force_vent(), 123 - self.angle_vent))
            vecteur2 = (-vecteur[0], - vecteur[1])
            trajectoire_derivee.append(self.deplacer_point(self.trajectoire[i], vecteur2))
        return trajectoire_derivee

    def calculer_trajectoire_initiale(self):
        """
        Calcule la trajectoire initiale du drone en fonction du vent.

        :return: La trajectoire initiale du drone.
        :rtype: list[(float, float)]
        """
        # Initialisation de la trajectoire dérivée
        trajectoire_initiale = [self.trajectoire[0]]
        # Parcours de la trajectoire
        for i in range(1, len(self.trajectoire)):
            # Ajout du point dérivé à la trajectoire dérivée
            trajectoire_initiale.append(self.deplacer_point(self.trajectoire[i], self.calculer_vecteur_resultant(
                self.calculer_vecteur_directeur(self.force_drone, self.calculer_angle(self.trajectoire[i - 1][0], self.trajectoire[i - 1][1], self.trajectoire[i][0], self.trajectoire[i][1])), self.calculer_vecteur_directeur(self.caluler_force_vent(), 123 - self.angle_vent))))
        return trajectoire_initiale

''' Exemple d'utilisation
drone = TrajectoiresDeriveeEtInitiale([(0, 0), (1, 5), (7, 5), (9, 7)], 5, 45.0, 0.024, 2.16 )
trajectoire_derivee = drone.calculer_trajectoire_derivee()
print("Trajectoire dérivée :", trajectoire_derivee)
trajectoire_initiale = drone.calculer_trajectoire_initiale()
print("Trajectoire initiale :", trajectoire_initiale)'''