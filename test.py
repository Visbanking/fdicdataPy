from fdicdata import (
    dataTaxonomy,
    getInstitutionsAll,
    getFailures,
    getFinancials,
    getHistory,
    getInstitution,
    getLocation,
    getSummary,
)

def test_functions():
    taxonomy = dataTaxonomy("institution")
    print(taxonomy)

    # get_institutions_all örneği
    institutions = getInstitutionsAll()
    print(institutions)

    # get_failures örneği
    failures = getFailures(['CERT'], date_range=('2010', '2015'))
    print(failures)

    # get_financials örneği
    financials = getFinancials(IDRSSD_or_CERT=37, metrics=["ASSET", "DEP"], limit=10, date_range=["2015-01-01", "*"])
    print(financials)

    # get_history örneği
    history = getHistory(CERT_or_NAME=3850, fields=["INSTNAME", "CERT", "PCITY", "PSTALP", "PZIP5"], CERT=True, limit=10)
    print(history)

    # get_location örneği
    location = getLocation(3850, fields=['NAME', 'CITY', 'ZIP'])
    print(location)

    # get_summary örneği
    summary = getSummary(states = ["California", "New York"], date_range= ["2020", "2021"], fields =  ["DEP", "ASSET"])
    print(summary)

    # get_institution örneği
    institution = getInstitution(name="Bank of America", fields=["NAME", "CITY", "STATE"], limit=10)
    print(institution)

if __name__ == "__main__":
    test_functions()
