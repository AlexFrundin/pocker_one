from xml.dom import minidom

doc=minidom.parse('task.xml')

doc.firstChild.firstChild.childNodes[0].firstChild.data

for task in doc.firstChild.firstChild.childNodes[0].firstChild.data:
    print(task.firstChild.data)


for task
