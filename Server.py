import socket
import threading
from Calculator import Calculator

class ThreadedServer(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # AF_INET - СОКЕТ ДЛЯ СЕТЕВОГО ПРОТОКОЛА IPv4
        # SOCK_STREAM - тип сокета; надёжная потокоориентированная служба (сервис) или потоковый сокет
        self.sock.bind((self.host, self.port))

    def listen(self):
        self.sock.listen(2)
        while True:
            try:
                client, address = self.sock.accept()
                print('connected: ', address)
                threading.Thread(target = self.listenToClient,args = (client,address)).start()
            except:
                self.sock.close()
                return False

    def listenToClient(self, client, address):
        size = 1024
        while True:
            try:
                data = client.recv(size)
                if data:
                    # Set the response to echo back the recieved data
                    uData=data.decode("utf-8")
                    print("client", address[1], '>', uData)
                    counts= str(uData)
                    f=str(Calculator.calc(self,counts))
                    client.send(f.encode("utf-8"))
            except:
                print("client", address[1], "discontected")
                client.close()
                return False

if __name__ == "__main__":
    while True:
        port_num = "50051"
        print("Port is",port_num)
        try:
            port_num = int(port_num)
            break
        except ValueError:
            pass

    ThreadedServer('',port_num).listen()