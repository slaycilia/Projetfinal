
# Projetfinal
# Projet Python - Trajectoire de Drone

Ce projet est réalisé par Facca Cécilia, Fleury Aurélien et Gruter Florian.
Il s'agit du projet final s'inscrivant dans le cours MGA802 (Étude de cas en aéronautique) de l'ETS à la session d'Été 2023.

## Description du projet
Ce projet Python vise à calculer et tracer la trajectoire d'un drone en fonction des points de passage et des conditions atmosphériques.

Il est divisé en plusieurs parties : 
- Récupération des données sur le vent en temps réel via le site https://openweathermap.org/
- Calcul de la trajectoire lissée du drône ;
- Calcul de la dérive exercée par le vent ;
- Calcul de la trajectoire que doit suivre le drône pour contrer le vent ;
- Affichage de la trajectoire du drône initiale, dérivée et corrigée ;
- Création de l'interface utilisateur avec tkinter.


## Fonctionnalités

- Permet à l'utilisateur de spécifier les points de passage du drone.
- Calcule la trajectoire initiale lissée du drone.
- Calcule la trajectoire déviée par le vent.
- Calcule la trajectoire finale du drone.
- Trace la trajectoire initiale, déviée et finale en 2D.

## Structure du projet

Le projet est organisé en plusieurs fichiers :

- `main.py` : Point d'entrée principal du programme. Il gère les paramètres généraux, obtient les points de passage de l'utilisateur, calcule les trajectoires et trace les résultats.
- `interface_utilisateur.py` : Contient la classe `InterfaceUtilisateur` qui gère l'interaction avec l'utilisateur pour obtenir les points de passage.
- `trajectoire.py` : Contient les classes `TrajectoireDrone2D` et `TrajectoiresDeriveeEtInitiale` qui effectuent les calculs de trajectoire.
-  `vent.py` : Contient la classe `Vent` qui effectue un appel a l'API de OpenWeatherMap pour connaitre les conditions actuelle du vent sur le lieu du vol.
-  `drone.py` : Contient la classe `Drone`qui contient les caracteristiques physique d'un drône.
## Dépendances

Le projet Python dépend des modules suivants :

- `numpy` : Utilisé pour manipuler des tableaux de données numériques.
- `matplotlib` : Utilisé pour tracer les graphiques de trajectoire.
- `tkinter` : Utilisé pour l'interface graphique.
- `math` : utilisé pour des calculs mathématiques.
- `requests`: utilisé pour la bibliothèque HTML.

## Configuration

Les paramètres généraux du projet peuvent être configurés dans le fichier `main.py` via l'interface graphique:
- `xmin`, `ymin`, `xmax`, `ymax` : Les limites de la zone que peut parcourir le drone (elles sont fixées mais modifiables).
- `vitesse_vent` : La vitesse du vent en m/s (via le module vent).
- `angle_vent` : L'angle du vent en degrés (via le module vent).
- `force_drone` : La force du drone.
- `surface_contact` : La surface de contact du drone.
- `masse_drone` : La masse du drone.
- `vitesse_drone` : La vitesse du drone.

Assurez-vous d'avoir les modules installés dans votre environnement Python pour exécuter le projet correctement via le fichier `requirements.txt`.

## Utilisation

1. Exécutez le fichier `main.py`.
2. Suivez les instructions pour entrer les points de passage du drone.
3. Le programme calculera la trajectoire initiale, la trajectoire déviée par le vent et la trajectoire finale.
4. Un graphique 2D sera affiché pour visualiser les trajectoires.

N'oubliez pas d'installer les dépendances requises avant d'exécuter le projet.
Pour toute documentation sur les fonction le fichier `index.html` permet d'afficher les docstreams.
Si vous avez des questions ou des problèmes, n'hésitez pas à nous contacter.

