from flask import Flask
import requests

app = Flask(__name__)

@app.route('/fire')
def get():
    requests.get("http://pyserver-service:5000/index")
    return 'hello world dummy'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9080, threaded = True)