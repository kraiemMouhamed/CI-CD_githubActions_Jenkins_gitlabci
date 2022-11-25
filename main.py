from requests import Request, Session
import json
import time
import webbrowser
import pprint

def getInfo (): # Function to get the info

    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest' # Coinmarketcap API url

    parameters = { 'slug': 'bitcoin', 'convert': 'USD' } # API parameters to pass in for retrieving specific cryptocurrency data

    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': '$SecretKey'
    } # SecretKey added in github secret namespaces

    session = Session()
    session.headers.update(headers)

    response = session.get(url, params=parameters)

    info = json.loads(response.text)

    pprint.pprint(info)
        
getInfo() # Calling the function to get the statistics