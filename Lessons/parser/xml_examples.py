import xml.etree.ElementTree as ET
#сщздаем корневой элемент с тегом root
root=ET.Element('todo')
#создаем вложенный тег
day=ET.SubElement(root, 'day')
day.set('date','01.01.18')
task1=ET.SubElement(day,'task')
task1.text='Wake up'
task2=ET.SubElement(day,'task')
task2.text='Make coffe'

tree=ET.ElementTree(root)

tree.write('task.xml')
