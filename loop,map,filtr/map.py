country_and_its_language = {
    'India': 'Hindi',
    'Australia': 'English',
    'South Africa': 'Afrikaans',
    'France': 'French',
    'United States': 'English'
}

def add_language(language):
    country = language['Country']
    if country in country_and_its_language:
        language['Language'] = country_and_its_language[country]
    else:
        language['Language'] = 'Unknown'  # or handle it differently if needed
    return language

# Example list of dictionaries with countries
ccc_list = [
    {'Country': 'India'},
    {'Country': 'Australia'},
    {'Country': 'Japan'},  # This will get 'Unknown' as language
    {'Country': 'France'}
]

cccl_list = list(map(add_language, ccc_list))

print(cccl_list)
