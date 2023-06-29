#On importe tous les dossiers
import interface_utilisateur
import atmospheric_drone
import trajectoire

## PARAMÈTRES GÉNÉRAUX
# Définition de la zone que peut parcourir le drône
xmin = 0
ymin = 0
xmax = 710.33
ymax = 673.15

# Résolution du lissage de la courbe
resolution = 100

# Informations recueillies sur le vent
latitude = 45.525520
longitude = -73.574279
api_key = "8ec08053eaf6e14d403ebe21404b6391"
vent = atmospheric_drone.Vent(latitude, longitude, api_key).mesure_du_vent()
vitess_vent = vent[0]
angle_vent = vent[1]


# Informations sur le drône
infos_drone = interface_utilisateur.DonneesDrone()
diametre = infos_drone.diametre
hauteur = infos_drone.hauteur
vitesse_drone = infos_drone.vitesse
masse_drone = infos_drone.masse
force_drone = atmospheric_drone.Drone(diametre, hauteur, vitesse_drone, masse_drone).trainee()
surface_contact = atmospheric_drone.Drone(diametre, hauteur, vitesse_drone, masse_drone).surface

##TRAJECTOIRE SOUHAITÉE INITIALEMENT

# Points par lequel le drône doit passer
points_passage = interface_utilisateur.InterfaceUtilisateur().points


# Graphique représentant la trajectoire souhaitée pour le drône
trajectoire_drone_ideale = trajectoire.TrajectoireDrone2D(points_passage, resolution)
traj_ini = trajectoire_drone_ideale.lisser_trajectoire()

## TRAJECTOIRE DÉVIEE PAR LE VENT

trajectoire_drone_derivee = trajectoire.TrajectoiresDeriveeEtInitiale(traj_ini, vitess_vent, angle_vent, surface_contact, force_drone)
traj_dev = trajectoire_drone_derivee.calculer_trajectoire_derivee()
traj_fin = trajectoire_drone_derivee.calculer_trajectoire_initiale()
tracer = trajectoire.AffichageTrajectoireDrone2D(points_passage, xmin, ymin, xmax, ymax).tracer_trajectoire_2D(traj_ini, traj_dev, traj_fin)