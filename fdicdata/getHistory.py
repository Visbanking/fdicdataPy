import io
import pandas as pd
import requests

# example: getHistory(CERT_or_NAME=3850, fields=["INSTNAME", "CERT", "PCITY", "PSTALP", "PZIP5"], CERT=True, limit=10)

def getHistory(CERT_or_NAME, fields, CERT=True, limit=10000):
    assert CERT_or_NAME is not None and fields is not None, "CERT_or_NAME and fields cannot be empty"
    
    url = f"https://banks.data.fdic.gov/api/history?"
    if CERT:
        url += f"filters=CERT%3A%20{CERT_or_NAME}"
    else:
        url += f"search=NAME%3A%20%27{CERT_or_NAME.replace(' ', '%20')}%27"
    url += f"&fields=CERT%2C{('%2C'.join(fields))}&limit={limit}&format=csv&download=false&filename=data_file"
    
    try:
        response = requests.get(url)
        df = pd.read_csv(io.StringIO(response.text))
        df = df.drop(["ID"], axis=1)
        return df
    except Exception as e:
        print(f"ERROR: {str(e)}")
        return None


