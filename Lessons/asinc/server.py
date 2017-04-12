import asyncio


@asyncio.coroutine
def handle(reader, writer):
    #reader and writer
    while True:
        data = yield from reader.read(1024)
        if not data:
            break
        print(data)
        writer.write(data)
        #озволяет передать все данные, передавая управление в основную программу
        yield from writer.drain()

loop = asyncio.get_event_loop()
#coroutine for server
coro=asyncio.start_server(handle, 'localhost', 5000, loop=loop)
#
server=loop.run_until_complete(coro)
#
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

#корректное завершение кода
server.close()
loop.run_until_complete(server.wait_closed())
loop.close()
