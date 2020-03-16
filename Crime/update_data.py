import requests
import json
from pathlib import Path
#  
file_dir = Path("/home/dylan/GitProjects/CityOfBuffaloData/data")

PARAMS = {'$limit':1000000}
r = requests.get('https://data.buffalony.gov/resource/d6g9-xbgu.json',params=PARAMS)

with open(file_dir/'crime_data.json', 'w') as json_file:
     json.dump(r.json(), json_file)


