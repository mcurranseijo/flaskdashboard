import requests, json

url = "http://api.openweathermap.org/data/2.5/weather?q=peoria&appid=0dfe70372466a9413e172216b72bad27&units=Imperial"

class Weather(object):
    def __init__(self):
        scope = "user-library-read user-read-currently-playing user-read-playback-state"
        self.weather_data = {
            'description': "n/a",
            'temp': "n/a",
            'high': "n/a",
            'low': "n/a",
            'url': "n/a"
        }

    def state(self):
        try:
            data = requests.get(url)
            data = json.loads(data.text)
            self.weather_data = {
                'description': data['weather'][0]['main'],
                'temp': data['main']['temp'],
                'high': data['main']['temp_max'],
                'low': data['main']['temp_min'],
                'url': f"http://openweathermap.org/img/wn/{data['weather'][0]['icon']}@4x.png"

            }
        except:
            pass
        return self.weather_data
