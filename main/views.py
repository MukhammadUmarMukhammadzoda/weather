from django.shortcuts import render
import requests as r
import math
import json
from django.http import HttpResponse
import datetime
import calendar
# Create your views here.
#Api getting part




def index(request):
    dt = datetime.datetime.today()
    date = dt.day
    month = dt.month
    m = calendar.month_name[month]
    full = str(date) + ' ' + str(m)
    now = datetime.datetime.now()
    day = now.strftime("%A")
    if request.method == 'POST':
        try:
           city = request.POST.get('city')
           api_key = 'a55396f3eb34ec444b88755d0bedf7a7'
           api = 'https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid='+api_key
           ans = r.get(api)
           ansj = ans.json()
           temp = ((ansj['main']['temp']) - 273.15)
           temp = round(temp)
           context = {'havo':temp,
                       'city':city,
                       'sana':full,
                       'kun':day}

        except :
            temp = 'Unknown Error!!'    
            context = {'havo':temp,
                       'sana':full,
                       'kun':day
                       }

        return render(request,'index.html',context)
    
    return render(request,'index.html')    
   
