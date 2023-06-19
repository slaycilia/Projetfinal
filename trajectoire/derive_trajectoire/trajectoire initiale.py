import numpy as np
import math

def calul_force_vent(vitesse_vent, surface_contact):
    densite_air = 1.2
    force_vent = 0.5 * densite_air * vitesse_vent**2 * surface_contact
    return force_vent

def calculer_angle(x1, y1, x2, y2):
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

def calcul_temps(x1, y1, x2, y2, vitesse_drone, temps_init):
    temps_final = temps_init + np.sqrt((x2 - x1)**2 + (y2 - y1)**2) / vitesse_drone
    return temps_final
def calcul_position_derivee(vitesse_vent, angle_vent, surface_contact, force_drone, masse_drone, temps1, vitesse_drone, x1, y1, x2, y2):
    force_vent = calul_force_vent(vitesse_vent, surface_contact)
    force_drone_x = force_drone * np.cos(math.radians(calculer_angle(x1, y1, x2, y2)))
    force_drone_y = force_drone * np.sin(math.radians(calculer_angle(x1, y1, x2, y2)))
    force_vent_x = force_vent * np.sin(math.radians(angle_vent - 33))
    force_vent_y = force_vent * np.cos(math.radians(angle_vent - 33))
    temps2 = calcul_temps(x1, y1, x2, y2, vitesse_drone, temps1)
    position_derive_x = x2 + ((force_drone_x - force_vent_x) / masse_drone) * ((temps2**2 - temps1**2) / 2)
    position_derive_y = y2 + ((force_drone_y - force_vent_y) / masse_drone) * ((temps2**2 - temps1**2) / 2)
    return (position_derive_x, position_derive_y)

def calcul_position_initiale(vitesse_vent, angle_vent, surface_contact, force_drone, masse_drone, temps1, vitesse_drone, x1, y1, x2, y2):
    force_vent = calul_force_vent(vitesse_vent, surface_contact)
    force_drone_x = force_drone * np.cos(math.radians(calculer_angle(x1, y1, x2, y2)))
    force_drone_y = force_drone * np.sin(math.radians(calculer_angle(x1, y1, x2, y2)))
    force_vent_x = force_vent * np.sin(math.radians(angle_vent - 33 + 180))
    force_vent_y = force_vent * np.cos(math.radians(angle_vent - 33 + 180))
    temps2 = calcul_temps(x1, y1, x2, y2, vitesse_drone, temps1)
    position_initiale_x = x2 + ((force_drone_x - force_vent_x) / masse_drone) * ((temps2**2 - temps1**2) / 2)
    position_initiale_y = y2 + ((force_drone_y - force_vent_y) / masse_drone) * ((temps2**2 - temps1**2) / 2)
    return (position_initiale_x, position_initiale_y)

def calculer_trajectoire_initiale(trajectoire, vitesse_vent, angle_vent, surface_contact, force_drone, masse_drone, vitesse_drone):
    """Calcule la trajectoire initiale d'un drône en fonction du vent.

    Arguments:
        trajectoire (list): Liste de coordonnées de la trajectoire du drône.
                            Chaque coordonnée est représentée sous la forme (latitude, longitude).
        vitesse_vent (float): Vitesse du vent en m/s.
        angle_vent (float): Direction du vent en degrés (0° correspondant au nord, angle positif dans le sens horaire).
        surface_contact (float): Surface du drône en contact avec le vent en m².
        force_drone (float): Force de trainée du drône en N.
        masse_drone (float): Masse du drône en kg.
        vitesse_drone (float): Vitesse du drône en m/s.

    Returns:
        trajectoire_initiale (list): Liste de points représentant la trajectoire initale du drône.
              Chaque point est un tuple (latitude, longitude).
    """
    # Initialisation de la trajectoire dérivée
    trajectoire_initiale = [trajectoire[0]]
    temps = [0]
    # Parcours de la trajectoire
    for i in range(1, len(trajectoire)):
        temps.append(calcul_temps(trajectoire[i-1][0], trajectoire[i-1][1], trajectoire[i][0], trajectoire[i][1], vitesse_drone, temps[i-1]))
        # Ajout du point dérivé à la trajectoire dérivée
        trajectoire_initiale.append(calcul_position_initiale(vitesse_vent, angle_vent, surface_contact, force_drone, masse_drone, temps[i-1], vitesse_drone, trajectoire[i-1][0], trajectoire[i-1][1], trajectoire[i][0], trajectoire[i][1]))
    return trajectoire_initiale

def calculer_trajectoire_derivee(trajectoire, vitesse_vent, angle_vent, surface_contact, force_drone, masse_drone, vitesse_drone):
    """Calcule la trajectoire dérivée d'un drône en fonction du vent.

    Arguments:
        trajectoire (list): Liste de coordonnées de la trajectoire du drône.
                            Chaque coordonnée est représentée sous la forme (latitude, longitude).
        vitesse_vent (float): Vitesse du vent en m/s.
        angle_vent (float): Direction du vent en degrés (0° correspondant au nord, angle positif dans le sens horaire).
        surface_contact (float): Surface du drône en contact avec le vent en m².
        force_drone (float): Force de trainée du drône en N.
        masse_drone (float): Masse du drône en kg.
        vitesse_drone (float): Vitesse du drône en m/s.

    Returns:
        trajectoire_derivee (list): Liste de points représentant la trajectoire dérivée du drône.
              Chaque point est un tuple (latitude, longitude).
    """
    # Initialisation de la trajectoire dérivée
    trajectoire_derivee = [trajectoire[0]]
    temps = [0]
    # Parcours de la trajectoire
    for i in range(1, len(trajectoire)):
        temps.append(calcul_temps(trajectoire[i-1][0], trajectoire[i-1][1], trajectoire[i][0], trajectoire[i][1], vitesse_drone, temps[i-1]))
        # Ajout du point dérivé à la trajectoire dérivée
        trajectoire_derivee.append(calcul_position_derivee(vitesse_vent, angle_vent, surface_contact, force_drone, masse_drone, temps[i-1], vitesse_drone, trajectoire[i-1][0], trajectoire[i-1][1], trajectoire[i][0], trajectoire[i][1]))
    return trajectoire_derivee

import matplotlib.pyplot as plt

def tracer_trajectoires(trajectoire1, trajectoire2, trajectoire3):
    x1_coords = [point[0] for point in trajectoire1]
    y1_coords = [point[1] for point in trajectoire1]

    x2_coords = [point[0] for point in trajectoire2]
    y2_coords = [point[1] for point in trajectoire2]

    x3_coords = [point[0] for point in trajectoire3]
    y3_coords = [point[1] for point in trajectoire3]

    plt.plot(x1_coords, y1_coords, '-o', label='Trajectoire dérivée')
    plt.plot(x2_coords, y2_coords, '-o', label='Trajectoire initiale')
    plt.plot(x3_coords, y3_coords, '-o', label='Trajectoire')

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Trajectoires')
    plt.grid(True)
    plt.legend()
    plt.show()


# Exemple de trajectoire, vitesse du vent et direction du vent
trajectoire = [(0, 0), (1, 5), (7, 5), (9, 7)]
trajectoire_derive = [(0, 0), (0.8228100806580909, 4.799998571567067), (8.425102664643147, 4.409508731786501), (9.675067673043603, 7.220426835029858)]
vitesse_vent = 10.0  # m/s
angle_vent = 45.0  # degrés
force_drone = 2.16
surface_contact = 0.024
masse_drone = 1
vitesse_drone = 10

# Calcul de la trajectoire dérivée
trajectoire_derivee = calculer_trajectoire_derivee(trajectoire, vitesse_vent, angle_vent, surface_contact, force_drone, masse_drone, vitesse_drone)
trajectoire_initiale = calculer_trajectoire_initiale(trajectoire, vitesse_vent, angle_vent, surface_contact, force_drone, masse_drone, vitesse_drone)
# Affichage du résultat
print("Trajectoire derivée :",trajectoire_derivee)
print("Trajectoire initiale :", trajectoire_initiale)
tracer_trajectoires(trajectoire_derivee, trajectoire_initiale, trajectoire)