from django.shortcuts import render
import json
import urllib.request

# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        city_str = city.replace(' ', '%20')
        new_city = [word.capitalize() for word in city.split()]
        city = ' '.join(new_city)
        try:
            res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city_str+'&appid=35bed192a5b122829bd8299a7d8be01a').read()
            json_data = json.loads(res)
            data = {
            'country_code': str(json_data['sys']['country']),
            'coordinate': str(json_data['coord']['lon']) + ' ' +
            str(json_data['coord']['lat']),
            'temp': str(-273 + int(json_data['main']['temp']))+'ºC',
            'pressure': str(json_data['main']['pressure']),
            'humidity': str(json_data['main']['humidity']),
            }
        except:
            data = 'Not found'
        
        
    else:
        city = ''
        data = {}
    return render(request, 'index.html', {'city': city, 'data': data})