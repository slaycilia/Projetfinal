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
vitesse_vent = 20  # m/s
angle_vent = 50.0  # degrés
force_drone = 2.16
surface_contact = 0.024

# Informations sur le drône
masse_drone = 1
vitesse_drone = 60


##TRAJECTOIRE SOUHAITÉE INITIALEMENT

# Points par lequel le drône doit passer
points_passage = [(50, 600), (200, 200), (300, 500),(450,350), (600, 550)]
# Résolution du lissage de la courbe
resolution = 100
# Graphique représentant la trajectoire souhaitée pour le drône
trajectoire_drone_ideale = trajectoire.TrajectoireDrone2D(points_passage, resolution, xmin, ymin, xmax, ymax)
traj_ini = trajectoire_drone_ideale.lisser_trajectoire()

## TRAJECTOIRE DÉVIEE PAR LE VENT

trajectoire_drone_derivee = trajectoire.TrajectoiresDeriveeEtInitiale(traj_ini, vitesse_vent, angle_vent, surface_contact, force_drone)
traj_dev=trajectoire_drone_derivee.calculer_trajectoire_derivee()
traj_fin = trajectoire_drone_derivee.calculer_trajectoire_initiale()
tracer = trajectoire_drone_ideale.tracer_trajectoire_2D(traj_ini, traj_dev, traj_fin)

