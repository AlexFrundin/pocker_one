import xml.etree.ElementTree as ET

#from ControllerContact import Controller
import time

def MakeTree(obj):
    root=ET.Element('PhoneBook')
    day=ET.SubElement(root, 'day')
    currenttime=time.localtime()
    day.set('Date','{}:{:02}:{:02}:{:02}:{:02}'.format(currenttime.tm_year,currenttime.tm_mon,\
    currenttime.tm_mday,currenttime.tm_hour,currenttime.tm_min))
    length=ET.SubElement(day,'length')
    length.text=str((len(obj)))
    tag=[]
    #not like
    a=0
    contact=[]
    for i, (name,number) in enumerate(obj.get_contact()):
        contact.append(ET.SubElement(day,"contact{}".format(i)))
        tag.append(ET.SubElement(contact[i],'name'))
        tag[a].text=str(name)
        tag.append(ET.SubElement(contact[i],'number'))
        tag[a+1].text=str(number)
        a+=2
    tree=ET.ElementTree(root)
    tree.write('{}.xml'.format(obj.name))
    #tree.write('Phone.xml')
