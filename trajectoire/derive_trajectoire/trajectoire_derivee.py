import numpy as np
import math

class TrajectoireDerivee:
    def __init__(self, trajectoire, vitesse_vent, angle_vent, surface_contact, force_drone, masse_drone, vitesse_drone):
        self.trajectoire = trajectoire
        self.vitesse_vent = vitesse_vent
        self.angle_vent = angle_vent
        self.surface_contact = surface_contact
        self.force_drone = force_drone
        self.masse_drone = masse_drone
        self.vitesse_drone = vitesse_drone

    def calul_force_vent(self):
        densite_air = 1.2
        force_vent = 0.5 * densite_air * self.vitesse_vent**2 * self.surface_contact
        return force_vent

    def calculer_angle(self, x1, y1, x2, y2):
        delta_y = y2 - y1
        delta_x = x2 - x1
        m = delta_y / delta_x
        angle_rad = math.atan(m)
        angle_deg = math.degrees(angle_rad)
        return angle_deg

    def calcul_temps(self, x1, y1, x2, y2, temps_init):
        temps_final = temps_init + np.sqrt((x2 - x1)**2 + (y2 - y1)**2) / self.vitesse_drone
        return temps_final

    def calcul_position_derive(self, vitesse_vent, angle_vent, temps1, x1, y1, x2, y2):
        force_vent = self.calul_force_vent()
        force_drone_x = self.force_drone * np.cos(self.calculer_angle(x1, y1, x2, y2))
        force_drone_y = self.force_drone * np.sin(self.calculer_angle(x1, y1, x2, y2))
        force_vent_x = force_vent * np.sin(angle_vent - 33)
        force_vent_y = force_vent * np.cos(angle_vent - 33)
        temps2 = self.calcul_temps(x1, y1, x2, y2, temps1)
        position_derive_x = x2 + ((force_drone_x - force_vent_x) / self.masse_drone) * ((temps2**2 - temps1**2) / 2)
        position_derive_y = y2 + ((force_drone_y - force_vent_y) / self.masse_drone) * ((temps2**2 - temps1**2) / 2)
        return (position_derive_x, position_derive_y)

    def calculer_trajectoire_derivee(self):
        trajectoire_derivee = [self.trajectoire[1]]
        temps = [0]
        for i in range(1, len(self.trajectoire)):
            temps.append(self.calcul_temps(self.trajectoire[i-1][0], self.trajectoire[i-1][1], self.trajectoire[i][0], self.trajectoire[i][1], temps[i-1]))
            trajectoire_derivee.append(self.calcul_position_derive(self.vitesse_vent, self.angle_vent, temps[i-1], self.trajectoire[i-1][0], self.trajectoire[i-1][1], self.trajectoire[i][0], self.trajectoire[i][1]))
        return trajectoire_derivee




# Exemple d'utilisation de la classe

# Définition des paramètres
trajectoire = [(0, 0), (1, 5), (7, 5), (9, 7)]
vitesse_vent = 10.0  # m/s
angle_vent = 45.0  # degrés
force_drone = 2.16
surface_contact = 0.024
masse_drone = 1
vitesse_drone = 10

# Création de l'objet DroneTrajectory
drone_traj = TrajectoireDerivee(trajectoire, vitesse_vent, angle_vent, surface_contact, force_drone, masse_drone, vitesse_drone)

# Calcul de la trajectoire dérivée
trajectoire_derivee = drone_traj.calculer_trajectoire_derivee()

# Affichage du résultat
print("Trajectoire dérivée :", trajectoire_derivee)
