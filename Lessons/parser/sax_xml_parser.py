import xml.sax

parser = xml.sax.make_parser()
#описываю класс для передачи, переопределяю методы обязательные
class TaskContebtHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.is_task=False
        super().__init__()

    def startElement(self,name,attrs):
        if name=='task':
            self.is_task=True

    def characters(self, content):
        if self.is_task:
            print(content)

    def endElement(self, name):
        if name =='task':
            self.is_task = False

#говорю какой класс использовать для поиска
parser.setContentHandler(TaskContebtHandler())


#начинаю парсить 
parser.parse('task.xml')
