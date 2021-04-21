import lxml.etree as et

doc = et.parse('DATA/solar.xml')

for planet in doc.findall('.//planet'):
    print(planet.get('planetname'))
    for moon in planet.findall('moon'):
        print(f"    {moon.text}")
print('-' * 60)
jupiter = doc.find('.//planet[@planetname="Jupiter"]')
for moon in jupiter.findall('moon'):
    print(moon.text)
