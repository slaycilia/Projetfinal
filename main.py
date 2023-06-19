#On importe tous les dossiers
#import interface_utilisateur
#import atmospheric_drone
import trajectoire

# Tracé trajectoire

# Points de passage et autres données de test
points_passage = [(0, 0), (200, 135), (400, 500), (600, 230)]
resolution = 100
xmin = 0
ymin = 0
xmax = 710.33
ymax = 673.15

# Création de l'instance de la classe TrajectoireDrone2D
trajectoire_drone = trajectoire.TrajectoireDrone2D(points_passage, resolution, xmin, ymin, xmax, ymax)

# Tracé de la trajectoire
trajectoire_drone.tracer_trajectoire_2D()