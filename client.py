import socket
import logging
import uuid
from utils import generate_text

# Definimos la dirección IP del servidor y el puerto
HOST = '127.0.0.1'
PORT = 65432

identifier = uuid.uuid4()  # Using UUID (Universally Unique Identifier) for each client

logging.basicConfig(level=logging.INFO)

logging.info(f"Client Identifier: {identifier}")

# Create TCP socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))

    while True:
        entry = input("Type the size of the text string or 'exit' to finish: ")
        if entry.lower() == 'exit':
            break
        
        try:
            size = int(entry)
            text = generate_text(size)
            with open(f"chains.txt-{identifier}", "a") as file:
                file.write(text+"\n")
            client_socket.sendall(text.encode())  # Sending message to server
            data = client_socket.recv(10**6)      # Receiving message from server
            logging.info(f'Server answer:\n{data.decode()}')
        except ValueError:
            logging.error('The value must be an integer')