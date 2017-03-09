from xml.dom import minidom


def ParserTree_DOM(obj):
    doc=minidom.parse("{}.xml".format(obj.name))
    length = int(doc.getElementsByTagName('length')[0].firstChild.data)
    for i in range(length):
        #contact=doc.getElementsByTagName("contact{}".format(i))[0]
        name=doc.getElementsByTagName("name")[i].firstChild.data

        number=doc.getElementsByTagName("number")[i].firstChild.data
        yield (name,number)
