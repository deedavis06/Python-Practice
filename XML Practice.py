import xml.etree.ElementTree as ET 

data = ET.Element('Person')

element1 = ET.SubElement(data, 'Email')
data.append(element1)

sel_1 = ET.SubElement(element1, 'Employee Address')
sel_1.text = 'ddd@unt.ex.edu'
sel_2 = ET.SubElement(element1, 'Student Address')
sel_2.text = 'ddd1@my.unt.ex.edu'

tree = ET.ElementTree(data)
print(tree)