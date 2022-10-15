import xml.etree.ElementTree as ET 

data = ET.Element('Person')

element1 = ET.SubElement(data, 'Email')

ET.Subelement(element1, 'Field 1', name = 'Employee Address').text = 'ddd@unt.ex.edu'
ET.Subelement(element1, 'Field 2', name = 'Student Address').text = 'ddd1@my.unt.ex.edu'

tre = ET.ElementTree(data)
tre.write('XMLPractice.xml')
