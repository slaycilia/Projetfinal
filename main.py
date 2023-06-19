#On importe tous les dossiers
#import interface_utilisateur
#import atmospheric_drone
import trajectoire

## PARAMÈTRES GÉNÉRAUX
# Définition de la zone que peut parcourir le drône
xmin = 0
ymin = 0
xmax = 710.33
ymax = 673.15

# Informations recueillies sur le vent
vitesse_vent = 4.12  # m/s
angle_vent = 50.0  # degrés
force_drone = 2.16
surface_contact = 0.024

# Informations sur le drône
masse_drone = 1
vitesse_drone = 60


##TRAJECTOIRE SOUHAITÉE INITIALEMENT

# Points par lequel le drône doit passer
points_passage = [(0, 0), (200, 135), (400, 500), (600, 230)]
# Résolution du lissage de la courbe
resolution = 100
# Graphique représentant la trajectoire souhaitée pour le drône
trajectoire_drone_ideale = trajectoire.TrajectoireDrone2D(points_passage, resolution, xmin, ymin, xmax, ymax)
traj_ini = trajectoire_drone_ideale.lisser_trajectoire()
trajectoire_drone_ideale.tracer_trajectoire_2D()

## TRAJECTOIRE DÉVIEE PAR LE VENT

trajectoire_drone_derivee = trajectoire.TrajectoireDerivee(traj_ini, vitesse_vent, angle_vent, surface_contact, force_drone, masse_drone, vitesse_drone)
traj_dev=trajectoire_drone_derivee.calculer_trajectoire_derivee()
print("dev",traj_dev)
derive_drone = trajectoire.TrajectoireDrone2D(traj_dev, resolution, xmin, ymin, xmax, ymax)
derive_drone.lisser_trajectoire()
print(derive_drone)
derive_drone.tracer_trajectoire_2D()


# Tracé trajectoire
# Exemple d'utilisation de la classe

# Définition des paramètres
#trajectoire = [(0, 0), (1, 5), (7, 5), (9, 7)]

# Calcul de la trajectoire dérivée
#trajectoire_derivee = drone_traj.calculer_trajectoire_derivee()

# Affichage du résultat
#print("Trajectoire dérivée :", trajectoire_derivee)






