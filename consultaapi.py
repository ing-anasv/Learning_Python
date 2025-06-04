#Consulta api

import requests

response = requests.get("   https://api.chucknorris.io/jokes/random?")

if response.status_code == 200:
    data = response.json()
    print("Chiste aleatorio de Chuck Norris: ")
    print(data['value'])
else:
    print("Error al obtener el chiste")