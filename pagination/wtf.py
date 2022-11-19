import csv
from pprint import pprint

bus_stations = [
    {
        'Name': 'Name',
        'Street': 'Street',
        'District': 'District',
    }
]

with open('data-398-2018-08-30.csv', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        bus_stations.append({
            'Name': row['Name'],
            'Street': row['Street'],
            'District': row['District'],
        })

pprint(bus_stations[5])
