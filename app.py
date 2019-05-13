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
         res =  {"fulfillmentText": "Windows application development requires you to work with VB and C#, Getting your bascis right in either one language seems like a good deal. IDE which I would prefer is Visual Studio. Happy Learning! :)"}
     elif oss == 'android':
         res =  {"fulfillmentText": "Java and Kotlin go behind making an app for Andriod. The best way to start learning this is any one of the Google's course. Learning about databases and a little about how the web fuctions might help you in your future work. To make your work easier, check out Flutter. Happy Learning :)"}
     elif oss == 'mac':
         res =  {"fulfillmentText": "Swift is a programming language used by developers to make application for the osX. It closely relates to C# and Java. However, learning only Swift will confine you to the Apple ecospace. I would suggest to pick up another language alongwith Swift for instance, Java, Python, C# or JavaScript. Happy Learning :) "}
     elif oss == 'apple':
         res =  {"fulfillmentText": "Making an app for the Apple Store is real biggie. Languages like Swift should help you make the most beautiful apps in iOS. Happy learning :) "}
     elif oss == 'linux':
         res =  {"fulfillmentText": "C, Python, Pearl, Ruby and some of the languages you can pick up to make a Linux application. A firm command on the UNIX system and terminals is also suggested. Happy learning :)"}
     else:
         res =  {"fulfillmentText": "Python is light-weight all in one programming lanugage. It is being used in various fields and has a vast community. Starting off here will make your life a whole lot easier."}   
     res = json.dumps(res,indent=4)
     webhookreply = make_response(res)
     webhookreply.headers['Content-Type'] = 'application/json'
     return webhookreply


def startupTechGame():
     res = games()
     res = json.dumps(res,indent=4)
     webhookreply = make_response(res)
     webhookreply.headers['Content-Type'] = 'application/json'
     return webhookreply


def startupTechEle():
     res = {"fulfillmentText": "There has never been a single language used for programming robots and electronic devices. Many languages are used for that purpose and often enough more than one in a single project. Robots can be programmed using pretty much any programming language. C/C++ and Python are very common.As for Electronic devices, there are 2 groups. The first one being embeding a little code to a chip driver with a light-weight, low-level language, often Assembly or C. The second group is interfacing with the device, for this you can learn C/C++, Python, MatLab, Java."}
     res = json.dumps(res,indent=4)
     webhookreply = make_response(res)
     webhookreply.headers['Content-Type'] = 'application/json'
     return webhookreply

def startupNonTech():
     res = {"fulfillmentText": "HTML, CSS and JavaScript are the languages that will help you start off your website from scratch. Although if you just want to blog or simply make websites, using a Site generator is a better go. For instance, Wordpress or Wix."}
     res = json.dumps(res,indent=4)
     webhookreply = make_response(res)
     webhookreply.headers['Content-Type'] = 'application/json'
     return webhookreply


def startupNonTechAI():
     res = {"fulfillmentText": "Artifical Intelligence is growing field. You should probably consider Python or R as your goto languages. Companies values these developers too and there's a great job opportunity. Learning Maths and Statistics woul enhance your skill in this field. Happy learning :)"}
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
     res =  {"fulfillmentText": "Hacking and Cracking requires a lot of problem solving apporach to learn. There are no courses for these which would get you started off ASAP. Considering ethical hacking requires you to be a know-it-all in how systems function. SQL and Java with terminal interfaces and concepts of probablity may help to some extent. Another suggestion is to take a professional Ethical Hacking Course. Happy Learning :)"}
     res = json.dumps(res,indent=4)
     webhookreply = make_response(res)
     webhookreply.headers['Content-Type'] = 'application/json'
     return webhookreply

def startupNonTechEnterprise():
     res =  {"fulfillmentText": "Be it looking for job or better your self with another programing language, the market is under steady acceleration. Many enterprise can be made with Python or Java or C# or Javascript. Starting off with one of these languages gives you a headstart in your job interviews. Happy learning :) "}
     res = json.dumps(res,indent=4)
     webhookreply = make_response(res)
     webhookreply.headers['Content-Type'] = 'application/json'
     return webhookreply

def startupNonTechApps():
     req = request.get_json(silent= True, force= True)
     oss = req.get("queryResult").get("parameters").get("os")
    
     if oss == 'windows':
         res =  {"fulfillmentText": "Windows application development requires you to work with VB and C#, Getting your bascis right in either one language seems like a good deal. IDE which I would prefer is Visual Studio. Happy Learning! :)"}
     elif oss == 'android':
         res =  {"fulfillmentText": "Java and Kotlin go behind making an app for Andriod. The best way to start learning this is any one of the Google's course. Learning about databases and a little about how the web fuctions might help you in your future work. To make your work easier, check out Flutter. Happy Learning :)"}
     elif oss == 'mac':
         res =  {"fulfillmentText": "Swift is a programming language used by developers to make application for the osX. It closely relates to C# and Java. However, learning only Swift will confine you to the Apple ecospace. I would suggest to pick up another language alongwith Swift for instance, Java, Python, C# or JavaScript. Happy Learning :) "}
     elif oss == 'apple':
         res =  {"fulfillmentText": "Making an app for the Apple Store is real biggie. Languages like Swift should help you make the most beautiful apps in iOS. Happy learning :) "}
     elif oss == 'linux':
         res =  {"fulfillmentText": "C, Python, Pearl, Ruby and some of the languages you can pick up to make a Linux application. A firm command on the UNIX system and terminals is also suggested. Happy learning :)"}
     else:
         res =  {"fulfillmentText": "Python is light-weight all in one programming lanugage. It is being used in various fields and has a vast community. Starting off here will make your life a whole lot easier."}     
     res = json.dumps(res,indent=4)
     webhookreply = make_response(res)
     webhookreply.headers['Content-Type'] = 'application/json'
     return webhookreply




#Response functions
def websitesuite():
     return {"fulfillmentText": "Learn HTML, CSS, and Javascript. Before you do any kind of server-side programming, this is a must. You can't build a webpage without HTML, CSS makes it look pretty, and JS makes it dynamic. Also, it wouldn't hurt to add on some jQuery. Install a web server, or find a free web host online. You don't need to pay for one. You're still learning. Personally, I have a WAMP server running on my desktop since I don't put anything into production, and I advise you to do the same. Learn a server-side scripting language. For server side programming, Python is said to be the easiest to learn. PHP is the most well used server-side language. Ruby is an phenom. Get coding! I cannot stress this enough. Once you are confident with the basics, do check out Node.js and other popular Javascript modules. The only way to learn is by doing. You can't just read a book."}

def games():
     return {"fulfillmentText": "Programming a game is a hge task, "}


     


			
			
			

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print ("Starting app on port %d" %(port))

    app.run(debug=True, port=port, host='127.0.0.1')

