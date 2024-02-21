import socket
import sys
import json


class Client():
    def __init__(self, address):
        self.sock_address = address
        self.sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

    # 接続を開始する
    def start(self):
        print('connecting to {}'.format(self.sock_address))
        try:
            self.sock.connect(self.sock_address)
            print('接続しました')
        except socket.error as err:
            print(err)
            print('エラーです')
            sys.exit(1)

    # データを送信する
    def sendData(self, json_data):
        for i in range(len(json_data)):
            try:
                data = json.dumps(json_data[i]).encode()
                self.sock.sendall(data)
                self.sock.settimeout(1.0)
                # データの受信
                self.recvData()
            except Exception as err:
                print(err)

        print('closing socket')
        self.sock.close()
    # データを受信
    def recvData(self):
        try:
            while True:
                data = self.sock.recv(4094)
                if data:
                    print('Server response: ' + data.decode('utf-8'))
                else:
                    break

        except TimeoutError:
            print('Socket timeout, ending listening for server messages')
        except Exception as err:
            print(err)



def main():
    json_data = [
        {
            "method": "floor",
            "params": 3.22432321,
            "param_types": "double",
            "id":1
        },
        {        
            'method': 'reverse',
            'params': 'hello world',
            'param_types': 'str',
            'id':2
        },
        {
            "method": "nroot",
            "params": [27, 3],
            "param_types": ["int", "int"],
            "id": 3
        },
        {
            "method": "validAnagram",
            "params": ["silent", "listen"],
            "param_types": ["str", "str"],
            "id": 4
        },
        {
            "method": "sort",
            "params": ["toyota", "nissan", "mazda", "honda", "suzuki"],
            "param_types": "str[]",
            "id": 5
        }
    ]
        
        
    sock_address = "./socket_file"
    client = Client(sock_address)
    client.start()
    client.sendData(json_data)

if __name__ == '__main__':
    main()


