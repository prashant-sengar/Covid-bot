import os
from flask import (Flask,request, make_response)
import sms
from firedb import db_access

# Flask app should start in global layout
app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == "POST":
        req = request.get_json(silent=True, force=True)
        res = processRequest(req)
        res = json.dumps(res, indent=4)
        r = make_response(res)
        r.headers['Content-Type'] = 'application/json'
        return r

def processRequest(req):

    query_response = req["queryResult"]
    params=query_response.get('parameters')
    city=params.get('geo-city')
    id=int(params.get('number')) 
    print(city,'\n',id)   
    if(city!=None):
        res=send_text(city)
    if(id!=None):
        res=db_access(id)
    #res = get_data()
    return res


def db(id):
    res=db_access(id)
    print(res,'\n')
    if(res=='-1'):
        return {
            "fulfillmentText": "Doctor doesn't exist"
        }
    else:
        return {
            "fulfillmentText": "Welcome Dr."+res+". Please enter Patient ID"
        }       
   # query_response = req["queryResult"]
    sms.text()    

    res = get_data()

    return res


def send_text(city):
    sms.text(city)
def get_data():
    speech = "Your appointment has been made. Please check your texts."

    return {
        "fulfillmentText": speech
    }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    print ("Starting app on port %d" %(port))
    app.run(port=port, host='0.0.0.0')