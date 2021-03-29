from multiprocessing.managers import BaseManager
import socket

NETWORK_MOCK_CONTAINER_NAME = 'network_mock_container'
NETWORK_MOCK_MANAGER_ADDRESS = (NETWORK_MOCK_CONTAINER_NAME, 50000)
NETWORK_MOCK_MANAGER_AUTHKEY = b'123'


class NetworkMock():
    def __init__(self):
        self.receieved_messages = []
        HOST = ''                 # Symbolic name meaning all available interfaces
        PORT = 50007              # Arbitrary non-privileged port
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen(1)
            conn, addr = s.accept()
            self.conn = conn
            self.addr = addr
            #with conn:
            #    print('Connected by', addr)
            #    while True:
            #        data = conn.recv(1024)
            #        if not data: break
            #        conn.sendall(data)

    def send_massage(self):
        print("send message")

    def receieve_message(self):
        with self.conn:
            print('Connected by', self.addr)
            while True:
                data = self.conn.recv(1024)
                if not data: break
                #conn.sendall(data)
                self.receieved_messages.append(data)

def get_network_mock():
    return NetworkMock()


class NetworkMockManager(BaseManager): pass
NetworkMockManager.register("get_network_mock", get_network_mock)


def set_server():
    manager = NetworkMockManager(address=NETWORK_MOCK_MANAGER_ADDRESS,
                                 authkey=NETWORK_MOCK_MANAGER_AUTHKEY)
    manager.get_server().serve_forever()


def get_client():
    manager = NetworkMockManager(address=NETWORK_MOCK_MANAGER_ADDRESS,
                                 authkey=NETWORK_MOCK_MANAGER_AUTHKEY)
    manager.connect()
    return manager.get_network_mock()  # pylint: disable=no-member


if __name__ == '__main__':
    print("Setting NetworkMockManager server")
    set_server()
