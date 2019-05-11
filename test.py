import urllib
import json
import os

from flask import Flask
from flask import request
from flask import make_response
app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    print("Welcome")
    req = request.get_json(silent=True, force=True)
    print("Request:")
    print(json.dumps(req, indent=4))
    if req.get("queryResult").get("action") == "find.age":
        return findage()
    elif req.get("queryResult").get("action") == "puzzles.yes":
        return puzzleValidationYes()
    elif req.get("queryResult").get("action") == "puzzles.no":
        return puzzleValidationNo()
    elif req.get("queryResult").get("action") == "puzzle.maybe":
        return puzzleValidationMaybe()
    else:
        return {}
        

def findage():
    req = request.get_json(silent= True, force= True)
    age = req.get("queryResult").get("parameters").get("number")
    if(age<10):
        res = {"fulfillmentText": "You are a kid"}#scratch
    else:
        return {}
    res = json.dumps(res, indent=4)
    webhookreply = make_response(res)
    webhookreply.headers['Content-Type'] = 'application/json'   
    return webhookreply

def puzzleValidationYes():
     res = {"fulfillmentText": "C#/C++"}
     res = json.dumps(res,indent=4)
     webhookreply = make_response(res)
     webhookreply.headers['Content-Type'] = 'application/json'
     return webhookreply

def puzzleValidationNo():
     res = {"fulfillmentText": "Python"}
     res = json.dumps(res,indent=4)
     webhookreply = make_response(res)
     webhookreply.headers['Content-Type'] = 'application/json'
     return webhookreply

def puzzleValidationMaybe():
     res = {"fulfillmentText": "Java"}
     res = json.dumps(res,indent=4)
     webhookreply = make_response(res)
     webhookreply.headers['Content-Type'] = 'application/json'
     return webhookreply
     


			
			
			

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print ("Starting app on port %d" %(port))

    app.run(debug=True, port=port, host='127.0.0.1')

