import requests
import json

def script_creator():
    res = requests.get("https://covid19.mathdro.id/api/confirmed")
    res = res.json()

    count = 0
    for i in res:
        print(count)
        count+=i['confirmed']

    print(count)

script_creator()
