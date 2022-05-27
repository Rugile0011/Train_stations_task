import numpy as np

# the user enters the number of cities and the number of stations
number_of_cities = int(input("Enter number of cities:"))
cities_with_train_station = list(
    map(int, input("Enter cities with train station (use a space instead of a comma):").strip().split()))[
                            :number_of_cities]

# varify whether the entered stations are added to the list
print(cities_with_train_station)

# varify the last number of city and station
last_station = np.max(cities_with_train_station)
list_of_cities = list(range(0, number_of_cities))
last_city = np.max(list_of_cities)

# if the station placed outside our last city, it will not be identified
# stations numbers must be in the boundaries of our added cities, then we find station's places
if last_station > last_city:
    print(f"{last_station} station is not found")
    exit()
else:
    print("Stations is found")


# determined the maximum distance from any city to its nearest train station
def flatland_space_stations(number_of_cities, cities_with_train_station):
    cities_with_train_station = sorted(cities_with_train_station)
    res = cities_with_train_station[0]

    for ind in range(1, len(cities_with_train_station)):
        res = max(res, (cities_with_train_station[ind] - cities_with_train_station[ind - 1]) // 2)

        res = max(res, number_of_cities - 1 - cities_with_train_station[-1])

        return res


flatland_space_stations(number_of_cities, cities_with_train_station)
result = flatland_space_stations(number_of_cities, cities_with_train_station)
print("The maximum distance from any city to its nearest train station is " + str(result) + "km")

# check the functionality using asserts
if __name__ == "__main__":
    assert flatland_space_stations(number_of_cities=10, cities_with_train_station=[2, 5]) == 4
    assert flatland_space_stations(number_of_cities=20, cities_with_train_station=[1, 5, 9]) == 10
    print("ALL TESTS PASSED")
