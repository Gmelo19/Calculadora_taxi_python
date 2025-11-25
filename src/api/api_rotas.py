import requests

API_KEY = "eyJvcmciOiI1YjNjZTM1OTc4NTExMTAwMDFjZjYyNDgiLCJpZCI6ImQwZDVmNzRmZGVlNjQ5YjhhNDU3ZDJhY2MwNjJhNTRkIiwiaCI6Im11cm11cjY0In0="

def geocodificar(endereco):
    """Converte endereço em latitude/longitude."""
    url = "https://api.openrouteservice.org/geocode/search"

    params = {
        "api_key": API_KEY,
        "text": endereco,
        "size": 1
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        raise Exception("Erro na geocodificação: " + response.text)

    data = response.json()

    lat = data["features"][0]["geometry"]["coordinates"][1]
    lon = data["features"][0]["geometry"]["coordinates"][0]

    return lat, lon


def calcular_TD(origem, destino):
    """Calcula distância real e tempo estimado com maior confiabilidade."""
    
    url = "https://api.openrouteservice.org/v2/directions/driving-car"

    headers = {
        "Authorization": API_KEY,
        "Content-Type": "application/json"
    }

    body = {
        "coordinates": [
            [origem[1], origem[0]],
            [destino[1], destino[0]]
        ],
        "preference": "fastest"
    }

    response = requests.post(url, json=body, headers=headers)

    if response.status_code != 200:
        raise Exception("Erro na API de rotas: " + response.text)

    data = response.json()

    # Preferência 1: usar summary
    try:
        distancia_m = data["routes"][0]["summary"]["distance"]
        duracao_s = data["routes"][0]["summary"]["duration"]

        if duracao_s is None:
            raise Exception("Duration veio nulo no summary.")

    except:
        # Preferência 2: usar o primeiro segmento
        distancia_m = data["routes"][0]["segments"][0]["distance"]
        duracao_s = data["routes"][0]["segments"][0]["duration"]

    distancia_km = distancia_m / 1000
    duracao_min = duracao_s / 60

    return distancia_km, duracao_min
