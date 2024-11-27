import xml.etree.ElementTree as ET
data = '''
  <person>
    <name>Chuck</name>
    <phone type="intl">
      +1 734 303 4456
    </phone>
    <email hide="yes"/>
  </person>
'''

tree = ET.fromstring(data)
print(f'Name: {str(tree.find("name").text)}')
print(f'Attr: {str(tree.find("email").get("hide"))}')

input = '''
  <stuff>
    <users>
      <user x="2">
        <id>001</id>
        <name>Chuck</name>
      </user>
      <user x="17">
        <id>016</id>
        <name>Max</name>
      </user>
    </users>
  </stuff>
'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print('User count: ', len(lst))
for item in lst:
  print(f'Name: {item.find("name").text}')
  print(f'Id: {item.find("id").text}')
  print(f'Attribute: {item.get("x")}')

