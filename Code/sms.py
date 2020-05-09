
def text():
    from twilio.rest import Client 
 
    account_sid = 'ACf06f4f617c93c803975128f3ad2a8049' 
    client = Client(account_sid, auth_token) 
 
    message = client.messages.create( 
                              from_='+12058437583', 
                              messaging_service_sid='MG73b3aa77c9c36961ae6b900960f6162d',  
                              body='Your appointment is scheduled for tomorrow at 11am in Halet hospital, Kanpur',     
                              to='+918660488960' 
                               ) 
 
    print(message.sid)