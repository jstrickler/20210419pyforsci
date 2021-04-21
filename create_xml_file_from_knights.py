import lxml.etree as et

root = et.Element('knights')

with open('DATA/knights.txt') as knights_in:
    for raw_line in knights_in:
        name, title, color, quest, comment = raw_line.rstrip().split(':')
        e_knight = et.SubElement(root, 'knight', title=title)
        e_name = et.SubElement(e_knight, 'name')
        e_name.text = name
        et.SubElement(e_knight, 'color').text = color
        et.SubElement(e_knight, 'quest').text = quest
        et.SubElement(e_knight, 'comment').text = comment

print(et.tostring(root, pretty_print=True, xml_declaration=True).decode())

doc = et.ElementTree(root)
doc.write('knights.xml', pretty_print=True, xml_declaration=True,
          encoding="utf-8")

