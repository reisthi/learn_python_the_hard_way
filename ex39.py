states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'Calinfornia': 'CA',
    'New York': 'NY',
    'Michigan': 'MI',
}

cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville',
}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print('-' * 10)

print('Michigan has: ', cities[states['Michigan']])
print('Florida has: ', cities[states['Florida']])

print('-' * 10)

for state, abbrev in list(states.items()):
    print(f"{state} is avvreviaded {abbrev}")

print('-' * 10)
print('NY has: ', cities['NY'])
print('OR has: ', cities['OR'])

print('-' * 10)
state = states.get('Texas')

if not state:
    print("Sorry, no Texas.")

print('-' * 10)

city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is : {city}")
