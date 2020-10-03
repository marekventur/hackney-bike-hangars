import requests
from bs4 import BeautifulSoup
import json

res = requests.get('https://licences.hackney.gov.uk:7443/sf/control/viewhangars')
soup = BeautifulSoup(res.text, 'html.parser')
data = soup.select('#hangerData')[0]['value']
data_json = json.loads(data)
with open("hangars.json", "w") as f:
  f.write(json.dumps(data_json, indent=2))

features = []
for hangar in data_json["hangers"].values():
  features.append({
    "type": "Feature",
    "geometry": {
      "type": "Point",
      "coordinates": [ float(hangar["long"]), float(hangar["lat"])]
    },
    "properties": {
      "id": hangar["hanger_id"],
      "spaces": hangar["spaces"],
      "street": hangar["street"],
      "created": hangar["created"],
      "endOfLife": hangar["end_of_life"],
      "class": hangar["hanger_type"]["class"],
      "costPerYear": hangar["hanger_type"]["cost"]["Per Year"],
      "waitingList": hangar["waitingList"]
    }
  })

with open("hangars.geojson", "w") as f:
  f.write(json.dumps({
    "type": "FeatureCollection",
    "features": features
  }, indent=2))
