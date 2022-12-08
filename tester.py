import requests

x = requests.get(f'https://api.at.govt.nz/gtfs/v3/routes/ddd5f1e9f37a4521912acb647024c7b1')
# requests.head("ddd5f1e9f37a4521912acb647024c7b1")
print(x.text)