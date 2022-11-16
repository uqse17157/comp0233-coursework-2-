import csv
from pathlib import Path
from cities import City, CityCollection

def read_attendees_file(filepath: Path) -> CityCollection:
    cities = []
    with open(filepath, 'r') as files:
        file = csv.reader(files)
        next(file)
        for i in file:
            attendee,country,_,city,latitude,longitude,_=i
            city = City(city, country, int(attendee), float(latitude), float(longitude))
            cities.append(city)
    citycollection = CityCollection(cities)
    return citycollection

if __name__ == '__main__':
    list_of_cities = read_attendees_file(Path("attendee_locations.csv"))
    list_of_cities.plot_top_emitters(list_of_cities.cities[0], 7, True)

