import os
import tempfile
import requests
import yaml
import pandas as pd


def getTaxonomy(taxonomy):
    url = f"https://banks.data.fdic.gov/docs/{taxonomy}"
    response = requests.get(url)
    if response.status_code == 200:
        with open(os.path.join(tempfile.gettempdir(), taxonomy), "wb") as f:
            f.write(response.content)
            print(f"Downloaded {taxonomy} to {f.name}")
    else:
        print(f"Error downloading {taxonomy}. Status code: {response.status_code}")