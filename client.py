import socket
import sys
import json


class Client:
    def __init__(self, server_address, config_file):
        # Create a TCP/IP socket
        sockClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.config = json.load(config_file)

        # Connect the socket to the port where the server is listening
        server_address = (self.config['ip'], self.config['port'])
        print(sys.stdout, 'connecting to %s port %s' % server_address)
        sockClient.connect(server_address)

        try:

            # sending  data
            message = 'the connection has been successfully established'
            print(message)
            sockClient.sendall(message)

           # Procurando resposta da conexão
            received = 0
            expected = len(message)

            while received < expected:
                data = sockClient.recv(1024)
                received += len(data)
                print(sys.stdout, 'received data', data)
        finally:
            print(sys.stdout, 'closing socket')
            sockClient.close()
