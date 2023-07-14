import os
import tempfile
import requests
import yaml
import pandas as pd

# example: dataTaxonomy("institution")

def getTaxonomy(taxonomy):
    url = f"https://banks.data.fdic.gov/docs/{taxonomy}"
    response = requests.get(url)
    if response.status_code == 200:
        with open(os.path.join(tempfile.gettempdir(), taxonomy), "wb") as f:
            f.write(response.content)
            print(f"Downloaded {taxonomy} to {f.name}")
    else:
        print(f"Error downloading {taxonomy}. Status code: {response.status_code}")

def dataTaxonomy(name):
    if name not in ["institution", "location", "history", "summary", "failure", "financial"]:
        raise ValueError("name argument must be one of these: institution, location, history, summary, failure, financial")

    try:
        taxonomy_file = f"{name}_properties.yaml"
        getTaxonomy(taxonomy_file)
        yaml_path = os.path.join(tempfile.gettempdir(), taxonomy_file)
        with open(yaml_path, "r") as f:
            yaml_data = yaml.safe_load(f)

        institution_properties = pd.DataFrame(columns=["Name", "Title", "Description", "Type"])
        for prop_name in yaml_data["properties"]["data"]["properties"]:
            prop_data = yaml_data["properties"]["data"]["properties"][prop_name]
            type_val = prop_data.get("type", "")
            title_val = prop_data.get("title", "")
            desc_val = prop_data.get("description", "")
            binded = pd.DataFrame({"Name": [prop_name], "Title": [title_val], "Description": [desc_val], "Type": [type_val]})
            institution_properties = pd.concat([institution_properties, binded], axis=0, ignore_index=True)

        return institution_properties

    except Exception as e:
        print(f"ERROR: {e}")
        return None
