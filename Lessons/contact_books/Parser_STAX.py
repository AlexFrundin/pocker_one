from xml.dom import pulldom

def parserStax(obj, lst_el):
    doc=pulldom.parse('{}.xml'.format(obj.name))
    item=[]
    for event, node in doc:
        if event==pulldom.START_ELEMENT and node.tagName in lst_el:
            doc.expandNode(node)
            item.append(node.toxml())
        if len(item)==2:
            yield item
            item=[]
