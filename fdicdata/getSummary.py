import pandas as pd
import urllib

# example: getSummary(states = ["California", "New York"], date_range= ["2020", "2021"], fields =  ["DEP", "ASSET"])

def getSummary(states, date_range, fields, limit=10000):
    if len(date_range) != 2:
        raise ValueError("Date range should have two elements: start date and end date")
    if len(states) == 0:
        raise ValueError("Please provide at least one state")
    elif len(states) == 1:
        filters = f"filters=STNAME%3A%20%22{urllib.parse.quote(states[0])}%22%20AND%20YEAR%3A%5B%22{date_range[0]}%22%20TO%20%22{date_range[1]}%22%5D"
    else:
        state_filters = [f"STNAME%3A%20%22{urllib.parse.quote(state)}%22" for state in states]
        state_filter_str = "%20OR%20".join(state_filters)
        filters = f"filters=({state_filter_str})%20AND%20YEAR%3A%5B%22{date_range[0]}%22%20TO%20%22{date_range[1]}%22%5D"

    fields_str = "%2C".join(fields)
    url = f"https://banks.data.fdic.gov/api/summary?{filters}&fields=STNAME%2CYEAR%2CCB_SI%2C{fields_str}&sort_by=STNAME%2CYEAR&sort_order=DESC&limit={limit}&format=csv&download=false&filename=data_file"

    try:
        df = pd.read_csv(url)
        df.drop("ID", axis=1, inplace=True)
        return df
    except Exception as e:
        print(f"ERROR: {e}")
        return None


