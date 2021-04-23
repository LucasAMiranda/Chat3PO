import socket
import json


class Cliente:
    def __init__(self):
        with open('config.json', 'r') as config_file:
           # try:
                self.config = json.load(config_file)
            #except json.decoder.JSONDecodeError:
                self.client = dict()

        with open("config.json", 'w') as fp:
            json.dump(self.client, fp)

        # Create a TCP/IP socket
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def run(self):
        address = (self.client['ip'], self.client['port'])
        self.client.bind(address)

        # Connect the socket to the port where the server is listening
        self.client.connect(address)

        self.client.listen(self.client['max-connections'])

        self.client.accept()

    # Stop connections

    def stop(self):

        self.client.close()


    # Executable in port and ip , listining all connections in ports and conversations
try:
    client = Cliente()
    client.run()

    while not client.client._closed:
        pass
        ...
except Exception as error:
    print(error)
    client.stop()
    raise
