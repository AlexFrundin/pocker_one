import xml.sax
#пока не придумал, как возвращать элемент в виде списка
#потому что решение которое крутится в голове не элегантное
#не хочу в классе взывать методы класса-контроллера,
#можно переписать класс парсера по-другому
#вместо print - return or yield не работают в этом классе
#
class TaskContebtHandler(xml.sax.ContentHandler):
    def __init__(self,lst_el):
        self.is_tag=False
        self.el=lst_el
        super().__init__()

    def startElement(self,name,attrs):
        if name in self.el:
            self.is_tag=True

    def characters(self,content):
        if self.is_tag:
            print (content)

    def endElement(self,name):
        if name in self.el:
            self.is_tag=False

def parser_sax(obj):
    #стартует при импортировании, странно! пришлось запихнуть в функцию
    parser=xml.sax.make_parser()
    parser.setContentHandler(TaskContebtHandler(('name','number')))
    parser.parse('{}.xml'.format(obj.name))
