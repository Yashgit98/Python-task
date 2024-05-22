ccc_list = [
    {'Country': 'India', 'City': 'New Delhi', 'Continent': 'Asia'},
    {'Country': 'Australia', 'City': 'Canberra', 'Continent': 'Australia'},
    {'Country': 'South Africa', 'City': 'Cape Town', 'Continent': 'Africa'},
    {'Country': 'France', 'City': 'Paris', 'Continent': 'Europe'},
    {'Country': 'United States', 'City': 'Washington DC', 'Continent': 'North America'},
]
i = 0
while i < len(ccc_list):
    country = ccc_list[i]['Country']
    continent = ccc_list[i]['Continent']
    print(f'{country} belongs to {continent} Continent')
    i = i + 1