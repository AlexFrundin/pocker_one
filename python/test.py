#!/usr/bin/env python
from gi.repository import GLib, GObject

def qwe():
    print(1)
    GLib.timeout_add_seconds(5, qwe)

qwe()
try:
    GObject.MainLoop().run()
except KeyboardInterrupt: # got Ctrl-C
    pass

Код, основанный на "event loop", позволяет несколько функций исполнять вперемежку, в отличие от while True цикла, который блокирует весь поток:

#!/usr/bin/env python
import time
from time import time as timer

interval = 5
while True:
    time.sleep(interval - timer() % interval)
    print(1)


try:
    os.system('clear')
except:
    os.system('cls')


    if sys.platform=='win32':os.system('cls')
else:os.system('clear')
