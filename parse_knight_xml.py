import lxml.etree as et

doc = et.parse('knights.xml')
print(doc)

root = doc.getroot()
print(root, root.tag)

for knight in root.findall('knight'):
    title = knight.get('title')
    name = knight.findtext('name')
    quest = knight.findtext('quest')
    print(f"{title:5s} {name:9s} {quest}")


