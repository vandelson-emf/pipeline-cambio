import requests
from config import OPENWEATHER_API_KEY

url = 'https://api.openweathermap.org/data/2.5/weather'
parametros = {
    "q": "Recife, BR",
    "appid": OPENWEATHER_API_KEY,
    "units": "metric",
    "lang": "pt_br"
}

resposta = requests.get(url, params=parametros, timeout=10)
resposta.raise_for_status()
print ('Status:', resposta.status_code)
print (resposta.text)