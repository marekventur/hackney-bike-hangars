import requests
from bs4 import BeautifulSoup
import json

res = requests.get('https://licences.hackney.gov.uk:7443/sf/control/viewhangars')
soup = BeautifulSoup(res.text, 'html.parser')
data = soup.select('#hangerData')[0]['value']
with open("hangars.json", "w") as f:
    f.write(json.dumps(json.loads(data), indent=2))

