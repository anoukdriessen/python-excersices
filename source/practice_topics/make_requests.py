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
def convert(time):
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

    sunrise_is_at = convert(result["sunrise"])
    sunset_is_at = convert(result["sunset"])
    solar_noon_is_at = convert(result["solar_noon"])

    hours_today = round((int(result["day_length"]) / 60) / 60, 1)
    
    # print(result)
    now = datetime.now().strftime("%H:%M:%S")
    print(f"current time:\t{now}")
    print(f"sunrise time:\t{sunrise_is_at}")
    print(f"solar noon:\t{solar_noon_is_at}")
    print(f"sunset time:\t{sunset_is_at}")

    print(f"today is {hours_today} hours long")

sunrises_and_sunsets()        