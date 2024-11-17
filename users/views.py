from django.shortcuts import render

# Create your views here.
def signin(requste):
   return render(requste , 'signin-light.html')

def signup(requste):
   return render(requste , 'signup-light.html')

def account_security(requste):
   return render(requste , 'real-estate-account-security.html')

def account_info(requste):
   return render(requste , 'real-estate-account-info.html')
 
def account_notifications(requste):
   return render(requste , 'real-estate-account-notifications.html')

