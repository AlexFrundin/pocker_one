import xml.etree.ElementTree as ET

tree=ET.parse('task.xml')

#print(tree.findall('//task'))

for task in tree.findall('./day/task'):
    print(task.text)
