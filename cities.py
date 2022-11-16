from math import asin, sqrt, sin, cos
from typing import Dict, List, Tuple

from matplotlib import pyplot as plt


class City:
    def __init__(self, city, country, attendee, latitude, longitude):
        if  latitude < -90 or latitude > 90:
            raise ValueError('latitude in [-90,90]?')
        if longitude > 180 or longitude < -180:
            raise ValueError('longitude in [-180,180]?')
        if attendee < 0:
            raise ValueError('attendee in [0:]?')
        if type(attendee) != int :
            raise TypeError('attendee is an integer?')
        self.city = city
        self.country = country
        self.attendee = attendee
        self.latitude = latitude
        self.longitude = longitude

    def distance_to(self, other: 'City') -> float:
        if type(other) != City:
            raise TypeError('input a city?')
        return 2 * 6371 * asin(sqrt(
            sin((other.latitude - self.latitude) / 2) ** 2 + cos(self.latitude) * cos(other.latitude) * sin(
                (other.longitude - self.longitude) / 2) ** 2))

    def co2_to(self, other: 'City') -> float:
        if type(other) != City:
            raise TypeError('input a city?')
        distance = self.distance_to(other)
        if distance <= 1000:
            return 200 * distance * self.attendee
        elif distance > 1000 and distance <= 8000:
            return 250 * distance * self.attendee
        else:
            return 300 * distance * self.attendee

class CityCollection:
    def __init__(self, list_of_cities):
        self.cities = list_of_cities

    def countries(self) -> List[str]:
        countries=[]
        for i in self.cities:
            countries.append(i.country)
        set_countries=list(set(countries))
        set_countries.sort(key=countries.index)
        return set_countries

    def total_attendees(self) -> int:
        tmp = []
        for i in self.cities:
            tmp.append(i.attendee)
        return sum(tmp)

    def total_distance_travel_to(self, city: City) -> float:
        if type(city) != City:
            raise TypeError('input a city?')
        distance_travel_to = []
        for i in self.cities:
            tmp=city.distance_to(i)*i.attendee
            distance_travel_to.append(tmp)
        return sum(distance_travel_to)

    def travel_by_country(self, city: City) -> Dict[str, float]:
        if type(city) != City:
            raise TypeError('input a city?')
        tmp = {}
        for i in self.cities:
            if i.country in tmp.keys():
                tmp[i.country] += i.distance_to(city)
            else:
                tmp[i.country] = i.distance_to(city)
        return tmp

    def total_co2(self, city: City) -> float:
        if type(city) != City:
            raise TypeError('input a city?')
        tmp = []
        for i in self.cities:
            tmp.append(i.co2_to(city))
        return sum(tmp)

    def co2_by_country(self, city: City) -> Dict[str, float]:
        if type(city) != City:
            raise TypeError('input a city?')
        tmp = {}
        for x in self.cities:
            if x.country in tmp.keys():
                tmp[x.country] += x.co2_to(city)
            else:
                tmp[x.country] = x.co2_to(city)
        return tmp

    def summary(self, city: City):
        if type(city) != City:
            raise TypeError('input a city?')
        print(f"Host city: {city.city} ({city.country})")
        print(f"Total CO2: {int(self.total_co2(city))} tones")
        print(f"Total attendee travelling to {city.city} from {len(self.cities)} different cities: {self.total_attendees()}")

    def sorted_by_emissions(self) -> List[Tuple[str, float]]:
        result = [(x.city, self.total_co2(x))for x in self.cities]
        return sorted(result, key=lambda x: x[1])

    def plot_top_emitters(self, city: City, n: int, save: bool):
        if type(city) != City:
            raise TypeError('input a city?')
        emissions = [(k,v) for k,v in dict(sorted(self.co2_by_country(city).items(), key=lambda x: x[1], reverse=True)).items()]
        n_cities = [i[0]for i in emissions[:n]]
        n_co2 = [i[1]for i in emissions[:n]]
        rest_co2 = sum([i[1]for i in emissions[n:]])
        n_cities.append('Everywhere else')
        n_co2.append(rest_co2)
        plt.bar(n_cities, n_co2)
        plt.xticks(rotation=60)
        plt.title(f"Top emissions from each country(top 7)")
        plt.ylabel("Total emissions (tonnes CO2)")
        if save:
            plt.savefig(f"{city.city.lower().replace(' ','_')}.png")
        plt.show()


