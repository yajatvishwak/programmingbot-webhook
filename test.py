import urllib
import json
import os

from flask import Flask
from flask import request
from flask import make_response
app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))
    res = {
        "fulfillmentText": "This is a text response FUCKKKKKKKKKKKKKKKKKKKKKKKKKKK"
    }
    res = json.dumps(res, indent=4)
    r = make_response(res)
    
    r.headers['Content-Type'] = 'application/json'
    return r

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print ("Starting app on port %d" %(port))

    app.run(debug=True, port=port, host='127.0.0.1')

