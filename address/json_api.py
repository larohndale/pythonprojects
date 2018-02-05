import urllib.parse
import requests

main_api = 'http://maps.googleapis.com/maps/api/geocode/json?'
print("Type in an address to retrieve data from a particular location.")
print("Press 'q' or 'quit to exit")
while True:
    address = input('Address: ') 

    if address == 'quit' or address == 'q': 
        break

    url = main_api + urllib.parse.urlencode({'address': address})
    print(url)

    json_data = requests.get(url).json()

    json_status = json_data['status']
    print('API Status: ' + json_status)
    print()

    if json_status == 'OK':
        for each in json_data['results'][0]['address_components']:
            print(each["types"])

    if json_status == 'OK':
        for each in json_data['results'][0]['address_components']:
            print(each['long_name'])
    
        formatted_address = json_data['results'][0]['formatted_address']
        print()
        print(formatted_address)