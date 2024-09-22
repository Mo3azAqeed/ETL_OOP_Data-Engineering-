import requests


base_url="https://pokeapi.co/api/v2/"
Name="ditto"

def get_sample(Name):
    url=f"{base_url}/pokemon/{Name}"
    response=requests.get(url)
    print(response.status_code)
    return response.text()

import pandas as pd 
 pd.read_sql('SELECT int_column, date_column FROM test_data',
...             conn,
...             parse_dates={"date_column": {"format": "%d/%m/%y"}})
   int_column date_column
0           0  2012-11-10
1           1  2010-11-12