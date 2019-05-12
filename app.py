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
    elif req.get("queryResult").get("action") == "puzzles.maybe":
        return puzzleValidationMaybe()
    elif req.get("queryResult").get("action") == "startup.tech.website":
        return startupTechWebsite()
    elif req.get("queryResult").get("action") == "startup.tech.app":
        return startupTechApp()
    elif req.get("queryResult").get("action") == "startup.tech.game":
        return startupTechGame()
    elif req.get("queryResult").get("action") == "startup.tech.ele":
        return startupTechEle()
    elif req.get("queryResult").get("action") == "startup.nontech":
        return startupNonTech()
    elif req.get("queryResult").get("action") == "job.mlai":
        return startupNonTechAI()
    elif req.get("queryResult").get("action") == "job.games":
        return startupNonTechGames()
    elif req.get("queryResult").get("action") == "job.crypto":
        return startupNonTechCrypto()
    elif req.get("queryResult").get("action") == "job.enterprise":
        return startupNonTechEnterprise()
    elif req.get("queryResult").get("action") == "job.apps":
        return startupNonTechApps()
        
        
    else:
        return {}
        

def findage():
    req = request.get_json(silent= True, force= True)
    age = req.get("queryResult").get("parameters").get("number")
    if(age<=10):
        res = {"fulfillmentText": "What an age to pursue programming! Since you are still young, I would like to suggest you to start off with a very fun programming language! Scratch is a GUI based programming language. It will help you learn programming from the very basics. Once you feel confident, shift to Python. Python is a great language for everyone! "}#scratch
    else:
        return {}
    res = json.dumps(res, indent=4)
    webhookreply = make_response(res)
    webhookreply.headers['Content-Type'] = 'application/json'   
    return webhookreply

def puzzleValidationYes():
     req = request.get_json(silent= True, force= True)
     age = req.get("queryResult").get("outputContexts")[0]['parameters']['number']
     if(age > 10 and age <19):
         res = {"fulfillmentText": "Ah! Problem solving nature! C++/C# is the best language for someone like your nature. It is one of the most advanced and sophisticated programming languages. It's powerful, it requires skill to master but once you do, you form a divine knowledge of programming."}
     else:
         res = {}
     res = json.dumps(res,indent=4)
     webhookreply = make_response(res)
     webhookreply.headers['Content-Type'] = 'application/json'
     return webhookreply

def puzzleValidationNo():
     req = request.get_json(silent= True, force= True)
     age = req.get("queryResult").get("outputContexts")[0]['parameters']['number']
     if(age > 10 and age <19):
         res = {"fulfillmentText": "Puzzles are boring, programming isn't. Python is a great language to start from. It is easy to pick up(you just need a few hours to learn it) and vastly being used in major applications. Me(chatbot) is made in this language. It has a vast forum, so you'll never be alone"}
     else:
         res = {}
     res = json.dumps(res,indent=4)
     webhookreply = make_response(res)
     webhookreply.headers['Content-Type'] = 'application/json'
     return webhookreply

def puzzleValidationMaybe():
     req = request.get_json(silent= True, force= True)
     age = req.get("queryResult").get("outputContexts")[0]['parameters']['number']
     if(age>10 and age<19):
         res = {"fulfillmentText": "Java is a language for you! It is an OOPs, high performance, platform independent language. Learning java can give you a firm grasp on your basics. After learning this language, picking up any language is going to be a very easy task. Happy learning :)"}
     else:
         res = {}
     res = json.dumps(res,indent=4)
     webhookreply = make_response(res)
     webhookreply.headers['Content-Type'] = 'application/json'
     return webhookreply

def startupTechWebsite():
     res = websitesuite()
     res = json.dumps(res,indent=4)
     webhookreply = make_response(res)
     webhookreply.headers['Content-Type'] = 'application/json'
     return webhookreply


def startupTechApp():
     req = request.get_json(silent= True, force= True)
     oss = req.get("queryResult").get("parameters").get("os")
     res =  {"fulfillmentText": "Apps"}
     if oss == 'windows':
         res =  {"fulfillmentText": "windows app"}
     elif oss == 'android':
         res =  {"fulfillmentText": "android app"}
     elif oss == 'mac':
         res =  {"fulfillmentText": "mac app"}
     elif oss == 'apple':
         res =  {"fulfillmentText": "ios mob app"}
     elif oss == 'linux':
         res =  {"fulfillmentText": "linux app"}
     else:
         res =  {"fulfillmentText": "python"}   
     res = json.dumps(res,indent=4)
     webhookreply = make_response(res)
     webhookreply.headers['Content-Type'] = 'application/json'
     return webhookreply


def startupTechGame():
     res = {"fulfillmentText": "Game development lang"}
     res = json.dumps(res,indent=4)
     webhookreply = make_response(res)
     webhookreply.headers['Content-Type'] = 'application/json'
     return webhookreply


def startupTechEle():
     res = {"fulfillmentText": "Ele arudiono and raspberrypi development lang"}
     res = json.dumps(res,indent=4)
     webhookreply = make_response(res)
     webhookreply.headers['Content-Type'] = 'application/json'
     return webhookreply

def startupNonTech():
     res = {"fulfillmentText": "static websites generators"}
     res = json.dumps(res,indent=4)
     webhookreply = make_response(res)
     webhookreply.headers['Content-Type'] = 'application/json'
     return webhookreply


def startupNonTechAI():
     res = {"fulfillmentText": "ai lang"}
     res = json.dumps(res,indent=4)
     webhookreply = make_response(res)
     webhookreply.headers['Content-Type'] = 'application/json'
     return webhookreply

def startupNonTechGames():
     res = games()
     res = json.dumps(res,indent=4)
     webhookreply = make_response(res)
     webhookreply.headers['Content-Type'] = 'application/json'
     return webhookreply

def startupNonTechCrypto():
     res =  {"fulfillmentText": "game dev"}
     res = json.dumps(res,indent=4)
     webhookreply = make_response(res)
     webhookreply.headers['Content-Type'] = 'application/json'
     return webhookreply

def startupNonTechEnterprise():
     res =  {"fulfillmentText": "enterprise"}
     res = json.dumps(res,indent=4)
     webhookreply = make_response(res)
     webhookreply.headers['Content-Type'] = 'application/json'
     return webhookreply

def startupNonTechApps():
     req = request.get_json(silent= True, force= True)
     oss = req.get("queryResult").get("parameters").get("os")
     res =  {"fulfillmentText": "Apps"}
     if oss == 'windows':
         res =  {"fulfillmentText": "windows app"}
     elif oss == 'android':
         res =  {"fulfillmentText": "android app"}
     elif oss == 'mac':
         res =  {"fulfillmentText": "mac app"}
     elif oss == 'apple':
         res =  {"fulfillmentText": "ios mob app"}
     elif oss == 'linux':
         res =  {"fulfillmentText": "linux app"}
     else:
         res =  {"fulfillmentText": "python"}   
     res = json.dumps(res,indent=4)
     webhookreply = make_response(res)
     webhookreply.headers['Content-Type'] = 'application/json'
     return webhookreply




#Response functions
def websitesuite():
     return {"fulfillmentText": "Web suite Python html Css Js Databases and Node.js"}

def games():
     return {"fulfillmentText": "game dev"}


     


			
			
			

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print ("Starting app on port %d" %(port))

    app.run(debug=True, port=port, host='127.0.0.1')

