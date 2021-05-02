#Programmer: Ibitola Mayowa David
#Apache 2.0 license
import json
import requests

from pip._vendor.distlib.compat import raw_input

while True:
    ip = raw_input("Input IP Address: ")
    url = "http://ip-api.com/json/"
    response = requests.get(url + ip)
    values = json.loads(response.content)



    print('The IP: ' + ip)
    print('Uses the ISP ' + '"' + values['isp'] + '"' + ' called ' + values['as'])
    print('In the city ' + values['city'] + ' of the country ' + values['country'] + '(' + values['countryCode'] + ')')
    print('With Timezone: ' + values['timezone'])

    More = input('Need more information? 1. Yes 2. No \n')

    if More == '1' and 'Yes':
        print("You've chosen number 1")
        print('More Information: ')
        print('Region: ' + values['regionName'])
        print('Zip code: ' + values['zip'])
        print('Latitude: ' + str(values['lat']) + ' and ' 'Longitude: ' + str(values['lon']))
        print('Organization: ' + values['org'])
        print('Done.')
        break

    elif More == '2' and 'No':
        print("You've chosen number 2")
        print("Scan Complete")
        break

    else:
        break

#Programmer: Ibitola Mayowa David
#Apache 2.0 license


