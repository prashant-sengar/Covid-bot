import urllib
import json
import os
from flask import (Flask,request, make_response)
import sms

# Flask app should start in global layout
app = Flask(__name__)


# whenever you make request /webhook
# Following calls are made
# webhook ->
# -----------> Process requests
# ---------------------------->get_data()


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
   
   # query_response = req["queryResult"]
    sms.text()    
    
    res = get_data()

    return res


def get_data():
    speech = "Your appointment has been made. Please check your texts."

    return {
        "fulfillmentText": speech
    }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    print ("Starting app on port %d" %(port))
    app.run(port=port, host='0.0.0.0')