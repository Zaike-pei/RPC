import socket
import os
import json
import math
import threading


class Server:
    def __init__(self, socket_path):
        self.sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self.socket_path = socket_path

    def start(self):
        try:
            os.unlink(self.socket_path)
        except FileNotFoundError:
            pass
        
        print('Starting up on {}'.format(self.socket_path)) 

        self.sock.bind(self.socket_path)
        self.sock.listen(1)

        while True:
            conn, address = self.sock.accept()

            print('Accepted connection')
            # 新しいスレッドを作成
            client_thread = threading.Thread(target=self.recvMess, args=(conn,))
            client_thread.start()
            #self.recvMess(conn)
            #print('thread test text')

    # データの受取
    def recvMess(self, conn):
        try:
            while True:
                recv_data = conn.recv(1024).decode('utf-8')
                print('received data from client: {}'.format(recv_data))
                if recv_data:
                    # 値を返す関数
                    self.response(conn, recv_data)
                else:
                    print('no data')
                    break
        
        finally:
            print('closing current connetction')
            conn.close()

    # クライアントへjsonデータを返す
    def response(self, conn, recv_data):
        try:
            res = JsonProcessor.process(json.loads(recv_data))
            conn.sendall(res.encode())
        except Exception as err:
            print('error: {}'.format(err))
            err_mess = {"err": str(err)}
            conn.sendall(json.dumps(err_mess).encode())

class JsonProcessor:
    processor = {
        "floor": (lambda x: math.floor(x), "int"),
        "reverse": (lambda s: s[::-1], "string"),
        "sort": (lambda sarr: sorted(sarr), "string[]"),
        "nroot": (lambda arr: math.pow(arr[0],1/arr[1]), "double"),
        "validAnagram": (lambda sarr:sorted(sarr[0]) == sorted(sarr[1]), "bool")
    }

    def process(json_data):
        try:
            method = json_data["method"]
            params = json_data["params"]
            #param_types = json_data["param_types"]
            id = json_data["id"]
            res_results = JsonProcessor.processor[method][0](params)
            res_result_type = JsonProcessor.processor[method][1]
            response = {"result": res_results, "result_type": res_result_type, "id": id}

            return json.dumps(response)

        except Exception as err:
            print('err: {}'.format(err))
            response = {'err': str(err)}
            return json.dumps(response)


def main():
    socket_path = './socket_file'
    server = Server(socket_path)
    server.start()

    

if __name__ == '__main__':
    main()
