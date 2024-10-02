import requests
import pandas as pd

PAGE_SIZE=500
API_URLS =[
 'https://de.dhv-xc.de/api/fli/flights?fkto%5B%5D=11185&l-fkto%5B%5D=Metzingen&navpars=%7B%22start%22%3A0%2C%22limit%22%3A500%2C%22sort%22%3A%5B%7B%22field%22%3A%22FlightDate%22%2C%22dir%22%3A-1%7D%2C%7B%22field%22%3A%22BestTaskPoints%22%2C%22dir%22%3A-1%7D%5D%7D',
 'https://de.dhv-xc.de/api/fli/flights?fkto%5B%5D=11185&l-fkto%5B%5D=Metzingen&navpars=%7B%22start%22%3A500%2C%22limit%22%3A500%2C%22sort%22%3A%5B%7B%22field%22%3A%22FlightDate%22%2C%22dir%22%3A-1%7D%2C%7B%22field%22%3A%22BestTaskPoints%22%2C%22dir%22%3A-1%7D%5D%7D'
]


def flight_days():
    flight_days = []

    for url in API_URLS:
        r = requests.get(url)
        if r.status_code==200:
            response = r.json()
         #print(response['data'])
            df = pd.DataFrame(response['data'])
    
            flight_days.extend(df['FlightDate'].unique())

    return flight_days