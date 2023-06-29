import matplotlib.pyplot as plt

class AffichageTrajectoireDrone2D:
    def __init__(self, points_passage, xmin, ymin, xmax, ymax):
        self.points_passage = points_passage
        self.xmin = xmin
        self.ymin = ymin
        self.xmax = xmax
        self.ymax = ymax

    def tracer_trajectoire_2D(self, trajectoire_initiale, trajectoire_deviee, trajectoire_finale):
        #image = plt.imread('/Users/ceciliou/Document/ETS MTL/MGA802_ETE/Projetfinal/Projet/Sans titre/trajectoire/images/testimage.jpg')
        image = plt.imread(r'C:\Users\sifak\OneDrive\Documents\Cours\2022-2023\Session Eté\MGA802\Projet-final\Projetfinal\trajectoire\images\testimage.jpg')
        fig, ax = plt.subplots()
        ax.imshow(image, extent=[self.xmin, self.xmax, self.ymin, self.ymax], aspect='auto', alpha=0.5)

        x_rep, y_rep = zip(*self.points_passage)
        x_init, y_init = zip(*trajectoire_initiale)  # Séparer les coordonnées x et y de la trajectoire initiale
        x_liss, y_liss = zip(*trajectoire_deviee)  # Séparer les coordonnées x et y de la trajectoire lissée
        x_dev, y_dev = zip(*trajectoire_finale)  # Séparer les coordonnées x et y de la trajectoire déviée

        plt.plot(x_rep,y_rep, marker="o", label = "Points repères")
        plt.plot(x_init, y_init, marker='+', label='Trajectoire souhaitée')
        plt.plot(x_liss, y_liss, marker='+', label='Trajectoire déviéé')
        plt.plot(x_dev, y_dev, marker='+', label='Trajectoire finale')

        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Trajectoire du drone')
        plt.grid(True)
        plt.legend()
        plt.show()
