import math
import numpy as np

class TrajectoiresDeriveeEtInitiale:
    def __init__(self, trajectoire, vitesse_vent, angle_vent, surface_contact, force_drone):
        self.trajectoire = trajectoire
        self.vitesse_vent = vitesse_vent
        self.angle_vent = angle_vent
        self.surface_contact = surface_contact
        self.force_drone = force_drone
        '''trajectoire (list): Liste de coordonnées de la trajectoire du drône.
                                Chaque coordonnée est représentée sous la forme (latitude, longitude).
            vitesse_vent (float): Vitesse du vent en m/s.
            angle_vent (float): Direction du vent en degrés (0° correspondant au nord, angle positif dans le sens horaire).
            surface_contact (float): Surface du drône en contact avec le vent en m².
            force_drone (float): Force de trainée du drône en N.'''

    def calculer_vecteur_directeur(self, norme, angle_deg):
        # Convertir l'angle de degrés à radians
        angle_rad = math.radians(angle_deg)
        # Calculer les composantes x et y du vecteur
        x = norme * np.cos(angle_rad)
        y = norme * np.sin(angle_rad)
        # Retourner le vecteur directeur (x, y)
        return (x, y)

    def calculer_vecteur_resultant(self, vecteur1, vecteur2):
        # Calculer les composantes x et y du vecteur résultant
        x = vecteur2[0] + vecteur1[0]
        y = vecteur2[1] + vecteur1[1]
        # Retourner le vecteur résultant (x, y)
        return (x, y)

    def deplacer_point(self, point, vecteur):
        # Décomposer les coordonnées du point
        x, y = point
        # Décomposer les composantes x et y du vecteur
        dx, dy = vecteur
        # Calculer la nouvelle position du point déplacé
        nouvelle_position = (x + dx, y + dy)
        # Retourner la nouvelle position du point déplacé
        return nouvelle_position

    def caluler_force_vent(self):
        densite_air = 1.2
        force_vent = 0.5 * densite_air * self.vitesse_vent ** 2 * self.surface_contact
        return force_vent

    def calculer_angle(self, x1, y1, x2, y2):
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
        """Calcule la trajectoire dérivée d'un drône en fonction du vent.
        Retourne: trajectoire_derivee (list): Liste de points représentant la trajectoire dérivée du drône.
                  Chaque point est un tuple (latitude, longitude).
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
        """Calcule la trajectoire initiale d'un drône en fonction du vent.
        Retourne: trajectoire_initiale (list): Liste de points représentant la trajectoire initiale du drône.
                  Chaque point est un tuple (latitude, longitude).
        """
        # Initialisation de la trajectoire dérivée
        trajectoire_initiale = [self.trajectoire[0]]
        # Parcours de la trajectoire
        for i in range(1, len(self.trajectoire)):
            # Ajout du point dérivé à la trajectoire dérivée
            trajectoire_initiale.append(self.deplacer_point(self.trajectoire[i], self.calculer_vecteur_resultant(
                self.calculer_vecteur_directeur(self.force_drone, self.calculer_angle(self.trajectoire[i - 1][0], self.trajectoire[i - 1][1], self.trajectoire[i][0], self.trajectoire[i][1])), self.calculer_vecteur_directeur(self.caluler_force_vent(), 123 - self.angle_vent))))
        return trajectoire_initiale

# Exemple d'utilisation
drone = TrajectoiresDeriveeEtInitiale([(0, 0), (1, 5), (7, 5), (9, 7)], 5, 45.0, 0.024, 2.16 )
trajectoire_derivee = drone.calculer_trajectoire_derivee()
print("Trajectoire dérivée :", trajectoire_derivee)
trajectoire_initiale = drone.calculer_trajectoire_initiale()
print("Trajectoire initiale :", trajectoire_initiale)
