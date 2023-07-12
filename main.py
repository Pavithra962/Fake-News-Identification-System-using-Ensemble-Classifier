from flask import Flask
from flask import Flask, app, request
from flask_cors import CORS
import requests

app = Flask(__name__)
cors = CORS(app)
@app.route('/fake_news', methods=['GET','POST'])
def a():
    uri = request.json['uri']
    r = requests.post("http://b484-34-86-173-217.ngrok-free.app/fake_news", data={'uri':uri})
    return r.json()
    
if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)