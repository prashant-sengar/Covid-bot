
#data1={
#    'Name' : 'Karan',
#    'Age'  : 22,
#    'Travel' : 'Delhi',
#    'Contacts' : 'Rishabh, Arjun'

#}
#data2={
#    'Name ' : 'Prashant',
#    'ID'    : 123,
#}
#result=db.post('/Patient',data1)
#result=db.post('/Doctor',data2)

def db_access(id):
    from firebase import firebase
    db=firebase.FirebaseApplication("https://covid-chatbot-a96c4.firebaseio.com/",None)
    res=db.get('/Doctor','')
    #print("type of res is",type(res),'\n')
   # print(res)
    for i in res.values():
        if(i['ID']==id):
            return i['Name ']
    return '-1'
def db_add(data):
    from firebase import firebase
    db=firebase.FirebaseApplication("https://covid-chatbot-a96c4.firebaseio.com/",None)
    res=db.post('/Patient',data)
    print(res)


#print(result)