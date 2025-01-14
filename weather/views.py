from django.shortcuts import render,HttpResponse
import json
import requests
# Create your views here.
def weather(request):
    if request.method == 'POST':
        city=request.POST['city']
        source="http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=6f8bc920828a172a2629994eecaa4950"
        list_of_data = requests.get(source.format(city)).json()

        data = {
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon'])+ ' ' +str(list_of_data['coord']['lat']),
            "temp": round((list_of_data['main']['temp']-32) * 5.0/9.0,2),
            "humidity":str(list_of_data['main']['humidity'])
        }
    else:
        data={}
    return render(request,"weather.html",data)    