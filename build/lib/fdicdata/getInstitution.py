import io
import pandas as pd
import requests

# example: getInstitution(name="Bank of America", fields=["NAME", "CITY", "STATE"], limit=10)

def getInstitution(name=None, IDRSSD_or_CERT=None, fields=None, IDRSSD=True, limit=10000):
    assert fields is not None, "Fields cannot be empty"
    if name is not None and IDRSSD_or_CERT is not None:
        raise ValueError("Please use only 'name' or 'IDRRSD_or_CERT' parameter.")
    
    url = "https://banks.data.fdic.gov/api/institutions?"
    if name is not None:
        url += f"search=NAME%3A%20%27{name.replace(' ', '%20')}%27"
    elif IDRSSD_or_CERT is not None:
        if IDRSSD:
            url += f"filters=FED_RSSD%3A%20{IDRSSD_or_CERT}"
        else:
            url += f"filters=CERT%3A%20{IDRSSD_or_CERT}"
    else:
        raise ValueError("Please provide either 'name' or 'IDRSSD_or_CERT' parameter.")
    
    url += f"&fields=FED_RSSD%2CREPDTE%2C{('%2C'.join(fields))}&limit={limit}&format=csv&download=false&filename=data_file"
    
    try:
        response = requests.get(url)
        df = pd.read_csv(io.StringIO(response.text))
        df = df.drop(["ID"], axis=1)
        df = df.rename(columns={"FED_RSSD": "IDRSSD", "REPDTE": "DATE"})
        df["DATE"] = pd.to_datetime(df["DATE"], format="%m/%d/%Y")
        return df
    except Exception as e:
        print(f"ERROR: {str(e)}")
        return None


