import pandas as pd
import urllib.request

# example: getInstitutionsAll()

def getInstitutionsAll():
    
    url = "https://s3-us-gov-west-1.amazonaws.com/cg-2e5c99a6-e282-42bf-9844-35f5430338a5/downloads/institutions.csv"

    try:
        response = urllib.request.urlopen(url)
        df = pd.read_csv(response)
        return df
    except:
        print("ERROR: URL Changed please contact with package owner.")
        return None