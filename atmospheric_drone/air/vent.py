import requests

class Vent:
    def __init__(self, latitude, longitude, api_key):
        """
        Initialise une instance de la classe Vent.

        :param latitude: Latitude de la zone où vole le drone.
        :type latitude: float
        :param longitude: Longitude de la zone où vole le drone.
        :type longitude: float
        :param api_key: Clé API nécessaire pour récupérer les données.
        :type api_key: str
        """
        self.latitude = latitude
        self.longitude = longitude
        self.api_key = api_key

    def mesure_du_vent(self):
        """
        Effectue une mesure du vent en utilisant l'API OpenWeatherMap.

        La méthode récupère les données météorologiques à partir de l'API OpenWeatherMap
        en utilisant les coordonnées de latitude et de longitude fournies lors de
        l'initialisation de l'instance. Elle affiche ensuite la vitesse et la direction du vent.

        :return: None
        """
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={self.latitude}&lon={self.longitude}&appid={self.api_key}"
        print(url)
        response = requests.get(url)
        data = response.json()

        vitesse_vent = data['wind']['speed']
        direction_vent = data['wind']['deg']

        print(f"Wind Speed: {vitesse_vent} m/s")
        print(f"Wind Direction: {direction_vent}°")

# Coordonnées du point en 0,0 du repere local
latitude = 45.525520
longitude = -73.574279
api_key = "8ec08053eaf6e14d403ebe21404b6391"

vent = Vent(latitude, longitude,api_key)
vent.mesure_du_vent()