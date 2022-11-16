import pytest

from cities import *
from utils import *


class Test_City:
    def test_readdata(self):
        list_of_cities = read_attendees_file(Path("attendee_locations.csv"))
        assert 1

    def test_attendees_value(self):
        with pytest.raises(ValueError) as e:
            city = City('Zurich', 'Switzerland', -1, 47.22, 8.33)

    def test_attendees_type(self):
        with pytest.raises(TypeError) as e:
            city = City('Zurich', 'Switzerland', 25.3, 47.22, 8.33)

    def test_latitude_value(self):
        with pytest.raises(ValueError) as e:
            city = City('Zurich', 'Switzerland', 52, 360, 8.33)

    def test_longitude_value(self):
        with pytest.raises(ValueError) as e:
            city = City('Zurich', 'Switzerland', 52, 47.22, 360)

    def test_plot(self):
        list_of_cities = read_attendees_file(Path("attendee_locations.csv"))
        list_of_cities.plot_top_emitters(list_of_cities.cities[0], 7, True)
        assert 1

    def test_citycollections_type(self):
        with pytest.raises(TypeError) as e:
            list_of_cities = read_attendees_file(Path("attendee_locations.csv"))
            list_of_cities.total_distance_travel_to(10)

    def test_travel_by_country(self):
        list_of_cities = read_attendees_file(Path("attendee_locations.csv"))
        list_of_cities.travel_by_country(list_of_cities.cities[10])
        assert 1

    def test_sorted_by_emissions(self):
        list_of_cities = read_attendees_file(Path("attendee_locations.csv"))
        list_of_cities.sorted_by_emissions()
        assert 1

    def test_summary(self):
        list_of_cities = read_attendees_file(Path("attendee_locations.csv"))
        list_of_cities.summary(list_of_cities.cities[10])
        assert 1

    def test_co2_by_country(self):
        list_of_cities = read_attendees_file(Path("attendee_locations.csv"))
        list_of_cities.co2_by_country(list_of_cities.cities[10])
        assert 1

    def test_total_co2(self):
        list_of_cities = read_attendees_file(Path("attendee_locations.csv"))
        list_of_cities.total_co2(list_of_cities.cities[10])
        assert 1


if __name__ == '__main__':
    pytest.main("-s  test_cities.py")
