city1 = {
    'name': 'Moscow',
    'country': 'Russia',
    'population': 12_500_000
}

city2 = {
    'name': 'Los Angeles',
    'country': 'USA',
    'population': 3_900_000
}

city3 = {
    'name': 'Berlin',
    'country': 'Germany',
    'population': 3_600_000
}

city4 = {
    'name': 'Paris',
    'country': 'France',
    'population': 2_100_000
}

city5 = {
    'name': 'Kolkata',
    'country': 'India',
    'population': 4_500_000
}

cities_list = [city1, city2, city3, city4, city5]

for i, city in enumerate(cities_list):
    print(f"City {i + 1}: {city}")