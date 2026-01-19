from flask import Flask
import socket
import os

app = Flask(__name__)

@app.route('/')
def hello():
    # Получаем имя хоста (в Kubernetes это будет имя пода)
    pod_name = socket.gethostname()
    
    # Альтернативный способ через переменную окружения (если установлена)
    # pod_name = os.getenv('HOSTNAME', socket.gethostname())
    
    return f'Hello from Pod <b>{pod_name}</b>'

@app.route('/health')
def health():
    return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
