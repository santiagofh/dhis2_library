import os
import json
import requests
import pandas as pd

def get_data_to_dhis2(api_endpoint, baseUrl, username, password):
    session = requests.Session()
    session.auth = (username, password)
    api_url = baseUrl + api_endpoint
    headers = {"Content-Type": "application/json"}
    response = session.get(api_url, headers=headers)
    if response.status_code == 200:
        print("Los datos se han descargado exitosamente.")
        return pd.DataFrame(response.json())
    else:
        print("Se ha producido un error al consultar los datos.")
        print(response.text)
        return pd.DataFrame()

def get_attributes(row):
    attributes = {}
    for item in row['attributes']:
        attributes[item['attribute']] = item['value']
    return pd.Series(attributes)

