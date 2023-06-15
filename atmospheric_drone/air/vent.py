import requests



def mesure_du_vent(latitude,longitude,api_key="8ec08053eaf6e14d403ebe21404b6391"):


    url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}"
    print(url)
    response = requests.get(url)
    data = response.json()

    vitesse_vent = data['wind']['speed']
    direction_vent = data['wind']['deg']

    print(f"Wind Speed: {vitesse_vent} m/s")
    print(f"Wind Direction: {direction_vent}°")
"""Coordonnées du point en 0,0 du repere local"""
latitude = 45.525520
longitude = -73.574279
api_key = "8ec08053eaf6e14d403ebe21404b6391"
mesure_du_vent(latitude,longitude,api_key)
