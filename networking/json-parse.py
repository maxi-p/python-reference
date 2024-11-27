import json

data = '''
{
  "name" : "Chuck",
  "phone" : {
    "type": "intl",
    "number": "+1 734 303 4456"
  },
  "email": {
    "hide": "yes"
  }
}
'''

info = json.loads(data)
print(f'Name: {info["name"]}')
print(f'Hide: {info["email"]["hide"]}')

input = '''
[
  {
    "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  },
  {
    "id" : "016",
    "x" : "16",
    "name" : "Max"
  }
]
'''

print('') # Newline
info = json.loads(input)
print(f'User count: ', len(info))
for item in info:
  print(f'Name: {item["name"]}')
  print(f'Id: {item["id"]}')
  print(f'Attribute: {item["x"]}')
