from time import time
import requests
from datetime import datetime

# 1XX -> Hold on
# 2XX -> Success 
# 3XX -> Not allowed
# 4XX -> You made a mistake [404=not found]
# 5XX -> Server error

# International Space Station Current location
def iss():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    # print(response) # returns <Response [code]>

    # instead of writing if else statements like below
    # if response.status_code != 200:
        # error = response.status_code
        # print("An error happend")
        # if error == 404:
            # raise Exception("Resource does not exists")
        # elif error == 401:
            # raise Exception("You are not authorised to access this resouce")
        # else:
            # raise Exception("Bad response from API")
    # use raise for status method to handle exceptions
    response.raise_for_status()  

    # get data from response
    data = response.json()
    # print(data)

    # get specific items from data
    timestamp = data["timestamp"]
    print(datetime.fromtimestamp(timestamp))

    longtitude = data["iss_position"]["longitude"]
    latitude = data["iss_position"]["latitude"]
    position = (longtitude, latitude)

    # print(longtitude, latitude)
    print(position)

    # get your location from www.latlong.net
    longtitude = '6.110090'
    latitude = '52.777890'
    my_position = (longtitude, latitude)
    print(my_position)

# Sunset and Sunrise API
def convert_timeformat(time):
    new_time = time.split("T")[1].split("+")[0].split(":")
    new_time[0] = int(new_time[0]) + 2
    if(new_time[0] < 10):
        new_time[0] = "0" + str(new_time[0])
    # print(str(new_time[0]) + ":" + str(new_time[1]) + ":" + str(new_time[2]))
    return str(new_time[0]) + ":" + str(new_time[1]) + ":" + str(new_time[2])
def sunrises_and_sunsets():
    # request paramaters
        # lat (float) -> latitude in decimal degrees
        # lng (float) -> longtitude in decimal degrees
        # Optional: date (string YYYY-MM-DD) if not present -> current date
    
    # get your location from www.latlong.net
    longtitude = '6.110090'
    latitude = '52.777890'

    # response = requests.get(url=f"https://api.sunrise-sunset.org/json?lat={latitude}&lng={longtitude}&formatted=0")
    parameters = {
        "lat": latitude,
        "lng": longtitude,
        "formatted": 0
    }
    response = requests.get(url=f"https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()     # handle exceptions
    data = response.json()          # get data from request

    result = data['results']
    print(result)

    sunrise_is_at = convert_timeformat(result["sunrise"])
    sunset_is_at = convert_timeformat(result["sunset"])
    solar_noon_is_at = convert_timeformat(result["solar_noon"])

    hours_today = round((int(result["day_length"]) / 60) / 60, 1)
    
    # print(result)
    now = datetime.now().strftime("%H:%M:%S")
    print(f"current time:\t{now}")
    print(f"sunrise time:\t{sunrise_is_at}")
    print(f"solar noon:\t{solar_noon_is_at}")
    print(f"sunset time:\t{sunset_is_at}")

    print(f"today is {hours_today} hours long")

# OpenWeather API
def convert_time(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    if hour < 10:
        hour = "0" + str(hour)
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
      
    return "%s:%02d:%02d" % (hour, minutes, seconds)
def get_weather_data():
    url = "https://api.openweathermap.org/data/2.5/onecall"
    # get your location from latlong.net
    longtitude = '6.110090'
    latitude = '52.777890'
    # get your API key from openweathermap.org/
    key = '608402d16116042208e2dd7bc20af722'
    params = {
        "lat": latitude,
        "lon": longtitude,
        "appid": key,
        "exclude": 'minutely',
        "units": "metric",
        "lang": "nl"
    }
    response = requests.get(url=url, params=params)
    response.raise_for_status()     # handle exceptions
    data = response.json()          # get data from request

    print(data)
    
    offset = data['timezone_offset']
    current_data = {
        'now': convert_time(data['current']['dt'] + offset),
        'sunrise': convert_time(data['current']['sunrise'] + offset),
        'sunset': convert_time(data['current']['sunset'] + offset),
        'temp': data['current']['temp'],
        'humidity': data['current']['humidity'],
        'clouds': data['current']['clouds'],
        'wind_speed': data['current']['wind_speed'],
        'weather': data['current']['weather'][0]['description']
    }
    for key, value in current_data.items():
        if not (key == "now") and not (key == "weather"):
            out = f"[{key}]\t"
            value = str(value)
            if key == "temp":
                value = "\t" + value + " ℃"
            elif key == "humidity" or key == "clouds":
                value += " %"
            elif key == "wind_speed":
                value += " m/s"        
            out += value
        else:
            if key == "now":
                out = f"Het is {current_data['now']} en het is {current_data['weather']}" 
            else:
                out = ""   
        if out: print(out)
    print("**********************************************************************")
    hourly_data = data["hourly"]
    # data voor de komende 48 uur
    print(len(hourly_data), type(hourly_data))
    print("**********************************************************************")
    daily_data = data["daily"]
    # data voor
    print(len(daily_data), type(daily_data))
    print("**********************************************************************")
    try:
        print(data["alerts"])
    except KeyError:
        print("Geen alerts bekend voor nu")

# Test code below
# iss()
# sunrises_and_sunsets()        
get_weather_data()