import json
import math
import pandas as pd

input = "DATASET.json" 
output_xlsx = "dataset_xlsx.xlsx"
output_csv = "dataset_csv.csv"

with open(input, 'r', encoding='utf-8') as plik:
    dataset = json.load(plik)
    

def variables(dataset, nazwa):
    result = []
    for listing in dataset:
        val = listing.get(nazwa)

        if val:
            result.append(val)
        else:
            result.append(None)

    return result


def variable_coordinates(dataset, lat, long):
    result = []

    lat_centre = 52.2317194
    long_centre = 21.0060472

    for listing in dataset:
        latitude = listing.get(lat)
        longitude = listing.get(long)

        if latitude and longitude:
            lat_diff = lat_centre - latitude
            long_diff = long_centre - longitude

            delta_lat = lat_diff * 111.2
            delta_long = long_diff * 68.1

            distance = round(math.sqrt((delta_lat)**2 + (delta_long)**2),2)

            result.append(distance)
        else:
            result.append(None)

    return result

def varaible_age(dataset, nazwa):
    result = []
    for listing in dataset:
        build_year = listing.get(nazwa)
        year_now = pd.Timestamp.now().year

        if build_year:
            val = year_now - int(build_year)
            result.append(val)
        else:
            result.append(None)

    return result


export_data = {
    "cena": variables(dataset, "price"),
    "powierzchnia": variables(dataset, "area"),
    "wiek": varaible_age(dataset, "buildYear"),
    "czynsz": variables(dataset, "rentPrice"),
    "pokoje": variables(dataset, "rooms"),
    "piętro": variables(dataset, "floor"),
    "wysokość budynku": variables(dataset, "totalFloors"),
    "odległość od centrum": variable_coordinates(dataset, "latitude", "longitude"),
    "miasto": variables(dataset, "city"),
    "zabudowa": variables(dataset, "buildingType"),
    "wykończenie": variables(dataset, "condition"),
    "okna": variables(dataset, "windowsType"),
    "ogrzewanie": variables(dataset, "heating")
}

df = pd.DataFrame(export_data)

df.to_excel(output_xlsx, index=False)
df.to_csv(output_csv, index=False)

print(df)
