import requests

# r = requests.get('https://swapi.co/api/people/3/')
# print(r.json())

response = requests.get("http://api.open-notify.org/astros.json")

response_data = response.json()

people = response_data['people']

for n in range(len(people)):
    print(next(person['name'] for person in people))

