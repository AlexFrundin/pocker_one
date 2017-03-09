from xml.dom import pulldom

doc=pulldom.parse('task.xml')

for event, node in doc:
        if event==pulldom.START_ELEMENT and node.tagName =='task':
            doc.expandNode(node)
            print(node.toxml())


doc=pulldom.parse('task.xml')
for event, node in doc:
    print('event={},    node ={}'.format(event,node))
