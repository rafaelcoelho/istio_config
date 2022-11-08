from flask import Flask
import time
import sys

app = Flask(__name__)

@app.route('/index')
def get():
    time.sleep(5)
    return 'hello'

@app.route('/test')
def test():
    time.sleep(5)
    return 'hello world after'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', threaded = True)