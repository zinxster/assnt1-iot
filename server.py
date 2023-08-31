import asyncio
import websockets

messages = []

async def send_message(websocket, path):
    async for message in websocket:
        data = message.split(":")
        action = data[0]

        if action == "send":
            content = data[1]
            messages.append(content)
            await websocket.send("Message sent successfully!")
        elif action == "receive":
            await websocket.send("\n".join(messages))

start_server = websockets.serve(send_message, "localhost", 4000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
