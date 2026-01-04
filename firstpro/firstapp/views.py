from django.shortcuts import render
import datetime
from django.http import HttpResponse
# Create your views here.
def date_time_info(request):
    msg='<h1> Hello guys Very'
    date=datetime.datetime.now()
    hr=int(date.strftime('%H'))
    min=int(date.strftime('%M'))
    sec=int(date.strftime('%S'))
    if hr<12:
        msg+='Good Morning'
    elif hr<16:
        msg+='Good Afternoon'
    elif hr<21:
        msg+='Good Evening'
    else:
        msg+='Good Night'
    msg+='</h1> <hr>'
    msg+='<h1>Now the server Time is'+str(date)+'</h1>'
    return HttpResponse(msg)