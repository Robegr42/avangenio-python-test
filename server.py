import asyncio
import logging
import time
from utils import check_text

# Logger congiguration
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.FileHandler("server.log"),
                        logging.StreamHandler()
                    ])

logger = logging.getLogger('Server')

async def handle_client(reader, writer):
    addr = writer.get_extra_info('peername')
    logger.info(f'Conecction accepted from {addr}')

    while True:
        start_time = time.time()

        data = await reader.read(10**6)  # Reading bytes from client
        if not data:
            logger.info(f'Connection closed fron {addr}')
            break 
        
        message = data.decode()
        logger.info(f'Recieved: {message}')
        vals = await check_text(message)

        end_time = time.time()

        ans_data = f"""
Message: {message}
Metric: {vals[1]}
Process completed in {(end_time-start_time):.2f} seconds\n"""

        if vals[0]:
            ans_data = """Double \'a\' rule detected""" + ans_data

        writer.write(ans_data.encode())  # Sending answer to client
        await writer.drain()  # Waiting for data to be sent



async def main():
    server = await asyncio.start_server(handle_client, '127.0.0.1', 65432)

    addr = server.sockets[0].getsockname()
    logger.info(f'Server listening at {addr}')

    async with server:
        await server.serve_forever()  # Keep server running

if __name__ == '__main__':
    asyncio.run(main())
