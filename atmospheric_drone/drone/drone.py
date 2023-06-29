class Drone:
    def __init__(self, diametre, hauteur, vitesse, masse):
        """
        Initialise une instance de la classe Drone.

        :param diametre: Diamètre du drone en mètres.
        :type diametre: float
        :param hauteur: Hauteur du drone en mètres.
        :type hauteur: float
        :param vitesse: Vitesse du drone en mètres par seconde.
        :type vitesse: float
        :param masse: Masse du drone en kilogrammes.
        :type masse: float
        """
        self.diametre = diametre
        self.hauteur = hauteur
        self.vitesse = vitesse
        self.masse = masse
        self.surface = self.diametre * self.hauteur

    def trainee(self, densite_air=1.2, coefficient_trainee=1.5):
        """
        Calcule la traînée du drone.

        La méthode calcule la traînée du drone en utilisant les paramètres
        de densité de l'air et de coefficient de traînée fournis en option. Si les valeurs
        ne sont pas spécifiées, les valeurs par défaut sont utilisées.

        :param densite_air: Densité de l'air en kg/m³. (Défaut: 1.2)
        :type densite_air: float
        :param coefficient_trainee: Coefficient de traînée du drone. (Défaut: 1.5)
        :type coefficient_trainee: float
        :return: La valeur de la traînée du drone.
        :rtype: float
        """
        trainee = 0.5 * densite_air * (self.vitesse ** 2) * self.surface * coefficient_trainee
        return trainee
