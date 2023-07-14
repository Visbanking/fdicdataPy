import pandas as pd
import requests

# example: getFailures(['CERT'], date_range=('2010', '2015'))

def getFailures(fields, date_range=None, limit=10000):
    import io 
    assert fields is not None, "Fields cannot be empty"
    if date_range is not None:
        assert len(date_range) == 2, "Date range must have two values"
        assert len(date_range[0]) == len(date_range[1]) == 4, "Date range values must be of length 4"
        assert date_range[0] <= date_range[1], "Invalid date range values"
        
    url = "https://banks.data.fdic.gov/api/failures?"
    if date_range is not None:
        url += f"filters=FAILYR%3A%5B%22{date_range[0]}%22%20TO%20%22{date_range[1]}%22%5D&"
    
    url += f"fields=CERT%2CNAME%2CFAILDATE%2C{'%2C'.join(fields)}&limit={limit}&format=csv&download=false&filename=data_file"
    
    try:
        response = requests.get(url)
        df = pd.read_csv(io.StringIO(response.text))
        df = df.assign(FAILDATE=pd.to_datetime(df["FAILDATE"], format="%m/%d/%Y")).drop("ID", axis=1)
        return df
    except Exception as e:
        print(f"ERROR: {str(e)}")
        return None
