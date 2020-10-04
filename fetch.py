import requests
from bs4 import BeautifulSoup
import json

res = requests.get('https://licences.hackney.gov.uk:7443/sf/control/viewhangars')
soup = BeautifulSoup(res.text, 'html.parser')
data = soup.select('#hangerData')[0]['value']
data_json = json.loads(data)
with open("hangars.json", "w") as f:
  f.write(json.dumps(data_json, indent=2))

def waiting_list_to_color(count):
  if (count == 0):
    return "#9CF168" # green
  if (count < 10):
    return "#F7EA4A"
  return "#E6696E"

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
      "waitingList": hangar["waitingList"],
      "marker-size": "small",
      "marker-symbol": "bicycle",
      "marker-color": waiting_list_to_color(hangar["waitingList"])
    }
  })

with open("hangars.geojson", "w") as f:
  f.write(json.dumps({
    "type": "FeatureCollection",
    "features": features
  }, indent=2))
