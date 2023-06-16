import matplotlib.patches as patches

#Classe qui permet de définir des obstacles dans l'espace

class Obstacle():
    def __init__(self, origine, longueur, largeur, rayon):
        self.origine = origine #point d'origine de l'obstacle
        self.longueur = longueur #longueur de l'obstacle selon l'axe x s'il s'agit d'un rectangle
        self.largeur = largeur #largeur de l'obstacle selon l'axe y s'il s'agit d'un rectangle
        self.rayon = rayon #Rayon de l'obstacle s'il s'agit d'un cercle

    def tracer_obstacle(self, graphique):
        """
        Ajout de l'obstacle sur le graphique représentant l'espace dans lequel évolue le drône
        :param graphique: graphique qui représente l'espace dans lequel évolue le drône
        :param origine: Point d'origine de l'obstacle
        :param longueur: Longueur de l'obstacle selon l'axe x (dans le cas où il s'agit d'un rectangle)
        :param largeur: Largeur de l'obstacle selon l'axe y (dans le cas où il s'agit d'un rectangle)
        :param rayon: Rayon de l'obstacle s'il s'agit d'un cercle
        :return: graphique avec l'obstacle ajouté
        """
        # Création du rectangle représentant l'obstacle
        if longueur > 0 and largeur > 0:
            rectangle = patches.Rectangle(origine, longueur, largeur, linewidth=1, edgecolor='r', facecolor='r')
            # Ajout du rectangle au graphique
            graphique.add_patch(rectangle)

        # Création d'un cercle représentant l'obstacle
        if rayon > 0:
            cercle = patches.Circle(origine, rayon, linewidth=1, edgecolor='r', facecolor='r')
            # Ajout du cercle sur le graphique
            graphique.add_patch(cercle)



