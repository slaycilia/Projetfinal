import matplotlib.pyplot as plt

from matplotlib.offsetbox import OffsetImage, AnnotationBbox

class PlotImage:
    def __init__(self, image_path, xmin, ymin, xmax, ymax):
        self.image_path = image_path
        self.xmin = xmin
        self.ymin = ymin
        self.xmax = xmax
        self.ymax = ymax

    def plot(self):
        # Création du plot
        fig, ax = plt.subplots()

        # Chargement de l'image
        image = plt.imread(self.image_path)

        # Affichage de l'image de fond
        ax.imshow(image, extent=[self.xmin, self.xmax, self.ymin, self.ymax], aspect='auto', alpha=0.5)

        # Tracer vos données sur le plot
        # ...

        # Affichage du plot
        plt.show()

image_path = 'testimage.jpg'
xmin = 0
ymin = 0
xmax = 710.33
ymax = 673.15

plot_image = PlotImage(image_path, xmin, ymin, xmax, ymax)
plot_image.plot()