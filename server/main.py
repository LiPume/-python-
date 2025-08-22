import asyncio
import json
import sys
import os
import platform

get_os = platform.system()
split_symbol = '\\' if get_os == 'Windows' else '/'

current_path = os.path.abspath(__file__)
top_path = split_symbol.join(current_path.split(split_symbol)[:-2])
sys.path.append(top_path)
from share.const import *
import game

g = game.Game()

async def handle_client(reader, writer):
    data = await reader.read(MAX_BYTES)
    msg = json.loads(data.decode())
    print(msg)
    s2cmsg = {}
    if msg['type'] == C2S_ADD_PLANT:
        s2cmsg = g.checkAddPlant(msg['pos'],msg['plant_idx'])
    elif msg['type'] == C2S_GET_PLANT:
        s2cmsg = g.getPlantInfo()

    writer.write(json.dumps(s2cmsg).encode())
    await writer.drain()

async def main():
    server = await asyncio.start_server(handle_client,'127.0.0.1',SERVER_PORT)
    print('Server start! Listen on port' ,SERVER_PORT)

    async with server:
        await server.serve_forever()

asyncio.run( main() )