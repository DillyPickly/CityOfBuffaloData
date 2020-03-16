import pandas as pd
from pathlib import Path

file_dir = Path("/home/dylan/GitProjects/CityOfBuffaloData/data")
df = pd.read_json(file_dir/'crime_data.json')
print(df)

