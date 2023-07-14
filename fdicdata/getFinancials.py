import io
import pandas as pd
import requests

# example: getFinancials(IDRSSD_or_CERT=37, metrics=["ASSET", "DEP"], limit=10, date_range=["2015-01-01", "*"])

def getFinancials(IDRSSD_or_CERT, metrics, limit=1, IDRSSD=True, date_range=None):
    assert IDRSSD_or_CERT is not None and metrics is not None, "IDRSSD_or_CERT and metrics cannot be empty"
    assert isinstance(IDRSSD_or_CERT, int), "IDRSSD_or_CERT must be a numeric value"
    if date_range is not None:
        assert len(date_range) == 2, "Date range must have two values"
    
    url = f"https://banks.data.fdic.gov/api/financials?filters={('RSSDID' if IDRSSD else 'CERT')}%3A%20{IDRSSD_or_CERT}"
    if date_range is not None:
        url += f"%20AND%20REPDTE%3A%5B{date_range[0]}%20TO%20{date_range[1]}%5D"
    url += f"&fields=RSSDID%2CREPDTE%2C{('%2C'.join(metrics))}&sort_by=REPDTE&sort_order=DESC&limit={limit}&offset=0&agg_term_fields=REPDTE&format=csv&download=false&filename=data_file"
    
    try:
        response = requests.get(url)
        df = pd.read_csv(io.StringIO(response.text))
        df = df.assign(DATE=pd.to_datetime(df["REPDTE"], format="%Y%m%d")).drop(["REPDTE", "ID"], axis=1).rename(columns={"RSSDID": "IDRSSD"})
        return df
    except Exception as e:
        print(f"ERROR: {str(e)}")
        return None


