const net = require('net');

class Client {
    constructor(address){
        this.client = net.createConnection(address);
        this.client.on('connect', () => {
            console.log("connected.");
        });
        this.client.on('data', (data) => {
            console.log("recieve data: " + data.toString());
        });
        this.client.on('end', () => {
            console.log('disconnected.');
        });
        this.client.on('error', (err) => {
            console.error(err.message);
        });
    }

    async write(data) {
        try {
            await new Promise((resolve, reject) => {
                this.client.write(data, (err) => {
                    if(err){
                        reject(err);
                    } else {
                        resolve();
                    }
                });
            });
        } catch (err) {
            console.log("err: " + data);
            throw err;
        }
    }   
    
    async sendData(data){
        for(let i = 0; i < data.length; i++){
            try {
                await this.write(JSON.stringify(data[i]));
                console.log("send data: " + JSON.stringify(data[i]));
                // 
                await new Promise((resolve) => setTimeout(resolve, 2000));
                
            } catch (e) {
                console.error("error!");
                throw error;
            }
        }

        this.client.end();
    }

}


jsonData = [
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
    
];

const address = './socket_file';
const client = new Client(address);
client.sendData(jsonData);