import matplotlib.pyplot as plt

class AffichageTrajectoireDrone2D:
    def __init__(self, points_passage, xmin, ymin, xmax, ymax):
        """
        Classe pour afficher la trajectoire 2D d'un drone à l'aide de matplotlib.

        :param points_passage: Les points de passage du drone.
        :type points_passage: list[(float, float)]
        :param xmin: Coordonnée x minimale de la zone d'affichage.
        :type xmin: float
        :param ymin: Coordonnée y minimale de la zone d'affichage.
        :type ymin: float
        :param xmax: Coordonnée x maximale de la zone d'affichage.
        :type xmax: float
        :param ymax: Coordonnée y maximale de la zone d'affichage.
        :type ymax: float
        """
        self.points_passage = points_passage
        self.xmin = xmin
        self.ymin = ymin
        self.xmax = xmax
        self.ymax = ymax

    def tracer_trajectoire_2D(self, trajectoire_initiale, trajectoire_deviee, trajectoire_finale):
        """
        Trace les trajectoires 2D du drone.

        :param trajectoire_initiale: La trajectoire initiale souhaitée.
        :type trajectoire_initiale: list[(float, float)]
        :param trajectoire_deviee: La trajectoire déviée.
        :type trajectoire_deviee: list[(float, float)]
        :param trajectoire_finale: La trajectoire finale.
        :type trajectoire_finale: list[(float, float)]
        """
        #image = plt.imread('/Users/ceciliou/Document/ETS MTL/MGA802_ETE/Projetfinal/Projet/Sans titre/trajectoire/images/testimage.jpg')
        image = plt.imread(r'C:\Users\sifak\OneDrive\Documents\Cours\2022-2023\Session Eté\MGA802\Projet-final\Projetfinal\trajectoire\images\testimage.jpg')
        fig, ax = plt.subplots()
        ax.imshow(image, extent=[self.xmin, self.xmax, self.ymin, self.ymax], aspect='auto', alpha=0.5)

        x_rep, y_rep = zip(*self.points_passage)
        x_init, y_init = zip(*trajectoire_initiale)  # Séparer les coordonnées x et y de la trajectoire initiale
        x_liss, y_liss = zip(*trajectoire_deviee)  # Séparer les coordonnées x et y de la trajectoire lissée
        x_dev, y_dev = zip(*trajectoire_finale)  # Séparer les coordonnées x et y de la trajectoire déviée

        plt.plot(x_rep, y_rep, marker="o", label="Points repères")
        plt.plot(x_init, y_init, marker='+', label='Trajectoire souhaitée')
        plt.plot(x_liss, y_liss, marker='+', label='Trajectoire déviée')
        plt.plot(x_dev, y_dev, marker='+', label='Trajectoire finale')

        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Trajectoire du drone')
        plt.grid(True)
        plt.legend()
        plt.show()
