from django.shortcuts import render

# Create your views here.
def account_notifications(requste):
   return render(requste , 'real-estate-account-notifications.html')