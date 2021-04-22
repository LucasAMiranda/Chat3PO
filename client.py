import socket
import json


class Cliente:
    def __init__(self):
        with open('config.json') as config_file:
            self.config = json.loads(config_file)

        # Create a TCP/IP socket
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect the socket to the port where the server is listening
        self.client.connect(client.run())
        self.client.accept()

    # Executable in port and ip , listining all connections in ports and conversations
    def run(self):

        msg = bytes(input("Digite algo: "), 'utf-8')

        self.client.send(msg)
        answer = self.config.recv(1024)
        print("Recebi mensagem ", answer)

        self.client.listen(
            self.config[{'ip': ''}], self.config[{'port': ''}], self.config[{'max-connections': ''}])

        for c in self.config[{'port'}]:
            print(c)

    # Stop connections
    def stop(self):
        self.client.close()


if __name__ == '__main__':
    try:
        client = Cliente()

        while not client.client._closed:
            pass
            ...

    except Exception as error:
        print(error)
        client.stop()
