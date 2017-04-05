from django.shortcuts import render
import requests 

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
from .models  import Customer , Account ,Card , cashWallet , transactionMode , transactionType ,transactionCategory ,Transaction , forexWallet ,forexTransactions , financialGoal , Currency

# Create your views here.
client_id='nipunyo@gmail.com'


def index(request):
    p =  requests.get('https://corporateapiprojectwar.mybluemix.net/corporate_banking/mybank/authenticate_client?client_id=nipunyo@gmail.com&password=JME2JRMV')
    p = json.loads(p.text)
    access_token = p[0]['token']
    r =  requests.get('https://retailbanking.mybluemix.net/banking/icicibank/participantmapping?client_id=nipunyo@gmail.com')
    a = json.loads(r.text)
    print a
    u = Customer.objects.get_or_create(CustomerID = client_id)[0]
    u.Name = 'Vishrut Kohli'
    u.Address = 'Bahawalpur CGHS , Dwarka , Delhi'
    u.Token  = access_token
    u.save()
    
    for i in a:
        try:
            if "debit card no" in i:
                v = u.account_set.get_or_create(accountNumber = i['account_no'] )[0]
                v.save()
                f =v.card_set.get_or_create(Type = 'debit')[0]
                f.cardNumber = i['debit card no']
                f.save()

        except Exception as e:
                    print e
                    pass


    try:
            if "Policy No" in i:
                v = u.loanspolicies_set.get_or_create(loanID = i['Policy No'] )[0]
                v.save()

    except Exception as e:
                    print e
                    pass                     
                    

    return HttpResponse('done')                 
        

def Transactions(request , cid):
    f = transactionCategory.objects.get_or_create(Category = 'Food')[0]
    l = transactionCategory.objects.get_or_create(Category = 'Luxary')[0]
    n = transactionCategory.objects.get_or_create(Category = 'Necessary')[0]

    u = Customer.objects.get_or_create(CustomerID = cid)[0]
    total = 0.0
    food = 0.0
    luxary = 0.0
    neccasary = 0.0
    extras = 0.0
    a = Transaction.objects.all().filter(CustomerID = u)
    for i in a:
        total = total + i.Ammount

        if i.Category == f:
            food = food + i.Ammount
            

        elif i.Category == l:
            luxary = luxary + i.Ammount
            
        elif i.Category == n:
            neccasary = neccasary + i.Ammount

        else :
            extras = extras + i.Ammount  


    print "food"  + str(food)
    print "luxary" + str(luxary)
    print "extras" + str(extras)

    print "nacess" +  str(neccasary)
    print total


    food_p = (food*100)/total
    luxary_p = (luxary/total)*100  
    neccasary_p = (neccasary/total)*100        
    extras_p = (extras/total)*100  

    print food_p
    print luxary_p

    q = {'food':food_p , 'luxary':luxary_p , 'necessary':neccasary_p , 'extras' : extras_p}
    print q
    q1 = json.dumps(q, indent = 4)


    



    return HttpResponse(q1 ,content_type = "application/json")    











