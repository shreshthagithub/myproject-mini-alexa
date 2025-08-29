import json
import requests
import pyttsx3

engine=pyttsx3.init()
city=input("Enter the name of the city: ")
url=f"http://api.weatherapi.com/v1/current.json?key=cc077bdf17dd40638f954516252006&q={city}&aqi=yes"
r=requests.get(url)
weather=json.loads(r.text)
temp_c= weather["current"]["temp_c"]
engine.say(f"The current tempearate in {city} is {temp_c} degree celcius")
# engine.say(weather)
engine.runAndWait()