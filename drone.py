import math

class Drone():
    def __init__(self, masse, envergure, vitesse_max, surface_alaire, coefficient_portance, coefficient_trainee, rayon_helice):
        self.masse = masse # en kg
        self.envergure = envergure # en m
        self.vitesse_max = vitesse_max # en m.s
        self.surface_alaire = surface_alaire # m²
        self.coefficient_portance = coefficient_portance
        self.coefficient_trainee = coefficient_trainee
        self.rayon_helice = rayon_helice # en m

    def poids(self, constante_gravitationnelle = 9.81):
        poids = self.masse * constante_gravitationnelle
        return poids

    def portance(self, densite_air = 1.2):
        portance = 0.5 * densite_air * (self.vitesse_max**2) * self.surface_alaire * self.coefficient_portance
        return portance

    def trainee(self,densite_air = 1.2):
        trainee = 0.5 * densite_air * (self.vitesse_max ** 2) * self.surface_alaire * self.coefficient_trainee
        return trainee

    def poussee(self, densite_air = 1.2):
        poussee = (self.vitesse_max**2) * 2 * math.pi * densite_air * (self.rayon_helice ** 2)
        return poussee


drone1 = Drone(masse=5, envergure=0.5, vitesse_max=50, surface_alaire=0.2, coefficient_portance=0.0015, coefficient_trainee=0.02, rayon_helice=0.001)
print(drone1.poussee(densite_air=1.2))
print(drone1.trainee(densite_air=1.2))
