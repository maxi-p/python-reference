import urllib.request, urllib.parse
import http, json, ssl

service_url = 'https://py4e-data.dr-chuck.net/opengeo?'

while True:
  address = input('Enter location: ')
  if (len(address) < 1): break

  address = address.strip()
  params = dict()
  params['q'] = address

  url = service_url + urllib.parse.urlencode(params)
  print(f'Retrieving {url}')
  uh = urllib.request.urlopen(url)
  data = uh.read().decode()
  data_type = str(data[:20]).replace('\n', '')
  print(f"Retrieved: {len(data)} characters {data_type}")

  js = json.loads(data)

  lat = js['features'][0]['properties']['lat']
  lon = js['features'][0]['properties']['lon']
  print(f'lat: {lat}, lon: {lon}')
  location = js['features'][0]['properties']['formatted']
  print(location)
