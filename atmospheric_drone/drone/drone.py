class Drone():
    def __init__(self, diametre, hauteur, vitesse, masse):
        self.diametre = diametre # en m
        self.hauteur = hauteur # en m
        self.vitesse = vitesse # en m.s
        self.masse = masse # en kg
        self.surface = self.diametre * self.hauteur

    def trainee(self,densite_air = 1.2, coefficient_trainee = 1.5):
        trainee = 0.5 * densite_air * (self.vitesse ** 2) * self.surface * coefficient_trainee
        return trainee