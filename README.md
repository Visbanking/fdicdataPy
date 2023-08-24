## Overview
The **fdicdata** package provides a set of functions for working with data from the Federal Deposit Insurance Corporation (FDIC), including retrieving financial data for FDIC-insured institutions and accessing the data taxonomy.

---

**Source Code**: <a target="_blank" href="https://github.com/Visbanking/fdicdataPy">https://github.com/Visbanking/fdicdataPy</a>

**Visbanking Website**: <a target="_blank" href="https://visbanking.com/">https://visbanking.com</a>

---

## Overview 

## Installation 
```python
pip install fdicdata
import fdicdata as fdic
```

## Examples 

```python
### Data Taxonomy:
fdic.dataTaxonomy("institution")

### Get Failures:
fdic.getFailures(['CERT'], date_range=('2010','2015'), name=("DORAL BANK"))

### Get Financials:
fdic.getFinancials(IDRSSD_or_CERT=37, metrics=["ASSET", "DEP"], limit=10, date_range=["2015-01-01", "*"])

### Get History:
fdic.getHistory(CERT_or_NAME=3850, fields=["INSTNAME", "CERT", "PCITY", "PSTALP", "PZIP5"], CERT=True, limit=10)

### Get Institutions:
fdic.getInstitution(IDRSSD_or_CERT='480228', fields=["NAME", "CITY", "STATE"], limit=10)

### Get Institutions All:
fdic.getInstitutionsAll()

### Get Location:
fdic.getLocation(3850)
fdic.getLocation(3850, fields=['NAME', 'CITY', 'ZIP'])

### Get Summary:
fdic.getSummary(states = ["California", "New York"], date_range= ["2020", "2021"], fields =  ["DEP", "ASSET"])
```

## License
This project is licensed under the terms of the MIT license.