from xml.dom import pulldom
import re
def parserStax(obj, lst_el):
    doc=pulldom.parse('{}.xml'.format(obj.name))
    item=[]
    for event, node in doc:
        if event==pulldom.START_ELEMENT and node.tagName in lst_el:
            doc.expandNode(node)
            item.append(pars_to_string(node.toxml()))
        if len(item)==2:
            yield item
            item=[]

def pars_to_string(item):
    reg=r'>[\w+ ]+<'
    return ''.join(re.findall(reg,item))[1:-1]
