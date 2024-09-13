from urllib.request import urlopen
import json
import pandas as pd
import requests

methods = ['car_data', 'drivers', 'intervals', 'laps', 'location', 'pit', 'position', 'race_control', 'sessions', 'stints', 'weather']

base_url = "https://api.openf1.org/v1/{method}?csv=true"

for method in methods:
    url = base_url.format(method=method)
    
    try:
        response = requests.get(url)

        response.raise_for_status()

        output_path = f'{method}.csv'
        
        with open(output_path, 'wb') as file:
            file.write(response.content)
        
        print(f"CSV data for '{method}' has been saved to {output_path}")
    
    except Exception as e:
        print(f"Failed to download or save data for '{method}': {e}")