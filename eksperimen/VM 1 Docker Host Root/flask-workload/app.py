from flask import Flask
import time, os

app = Flask(__name__)

@app.route('/')
def index():
    return "OK", 200

@app.route('/compute')
def compute():
    total = sum(i*i for i in range(1000000))
    return str(total), 200

@app.route('/io')
def io_task():
    with open('/tmp/testfile.txt', 'w') as f:
        f.write('test'*10000)
    return "IO Done", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
