import requests
import json
import random
import time
import csv

def script_creator():
    res = requests.get("https://covid19.mathdro.id/api/confirmed")
    res = res.json()

    data = {
            "type": "FeatureCollection",
            "features":[]
            }

    for i in res:
        data["features"].append(
                {
                    "type": "Feature",
                    "properties": {
                        "dbh":random.randint(-500,500)
                        },
                    "geometry": {
                        "type":"Point",
                        "coordinates": [i["lat"]*1.05,i["long"]*1.15][::-1]
                        }


                }
                )


    with open("data.json", "w") as fh, open("trees.geojson") as f2:
        json.dump(data,fh)


def csv_gen():
    days = [31,29,23]

    arr = []
    count = 0
    curr = 1

    for x in range(1,4):
        month = x

        for i in range(1, days[month-1]):
            str = "https://covid19.mathdro.id/api/daily/{0}-{1}-2020".format(i, month)

            res = requests.get(str)

            if res.status_code == 502:
                time.sleep(1)
                res = requests.get(str)
            # res = res.json()
            if res.status_code == 200:
                rxs = res.json()

                # print(str, res)

                for re in rxs:
                    # print(re["provinceState"],re["confirmed"])
                    count+=int(re["confirmed"])

            print("request made {}".format(curr))
            curr+=1

            if month!=1:
                arr.append([i+days[month-1],count])
            else:
                arr.append([i,count])

            print(str, res.status_code)
            # time.sleep(1)

    print(arr)

    with open("data.csv","w") as cs:
        writer = csv.writer(cs)
        arr.insert(0,["DayNumber", "Cases Till Date"])
        writer.writerows(arr)


if __name__=="__main__":
    csv_gen()

