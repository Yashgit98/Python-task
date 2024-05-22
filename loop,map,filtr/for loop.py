ccc_list = [
    {'Country': 'India', 'City': 'New Delhi', 'Continent': 'Asia'},
    {'Country': 'Australia', 'City': 'Canberra', 'Continent': 'Australia'},
    {'Country': 'South Africa', 'City': 'Cape Town', 'Continent': 'Africa'},
    {'Country': 'France', 'City': 'Paris', 'Continent': 'Europe'},
    {'Country': 'United States', 'City': 'Washington DC', 'Continent': 'North America'},
]
for values in ccc_list:
    country = values['Country']
    city = values['City']
    continent = values['Continent']

    print(f'{city} is the capital of {country}')