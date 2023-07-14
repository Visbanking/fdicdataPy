import pandas as pd

# example: getLocation(3850, fields=['NAME', 'CITY', 'ZIP'])

def getLocation(cert, fields=['NAME', 'CITY', 'STNAME'], limit=10000):
    url = f"https://banks.data.fdic.gov/api/locations?filters=CERT%3A{cert}&fields=CERT%2CNAME%2CESTYMD%2CMAINOFF%2C" \
          f"{('%2C').join(fields)}&limit={limit}&format=csv&download=false&filename=data_file"

    try:
        df = pd.read_csv(url, header=0)
        df['ESTYMD'] = pd.to_datetime(df['ESTYMD'], format="%m/%d/%Y")

        return df.drop(columns=['ID'])
    except Exception as e:
        print(f"ERROR: {str(e)}")
        return None
