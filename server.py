import socket
import json

class Server:
    def __init__(self):
        with open('config.json') as config_file:
            self.config = json.load(config_file)

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def run(self):
        address = (self.config['ip'], self.config['port'])

        self.server.bind(address)
        self.server.listen(self.config['max-connections'])

    def stop(self):
        self.server.close()

try:
    server = Server()
    server.run()

    while not server.server._closed:
        ...

except Exception as error:
    print(error)
    server.stop()