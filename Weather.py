import requests
import json 
import gtts
import playsound

c="Enter Your City"
sound = gtts.gTTS(c, lang="hi")
sound.save("Welcome1.mp3")
playsound.playsound("Welcome1.mp3")

city=input("Enter Your City: ")

url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID=097d3d14960c367133a5656fda03c666"

r=requests.get(url)

weather_dic=json.loads(r.text)
w=weather_dic["main"]["temp"]
wea=weather_dic["main"]["humidity"]

cen=w-32
ce=cen*0.56


we=f"The current weather in {city} is {ce} degree centigrade which is {w} degree fahrenheit and humidity is {wea}"
sound = gtts.gTTS(we, lang="en-IN")
sound.save("Welcome.mp3")
playsound.playsound("Welcome.mp3")

print("Temp in c: "+str(ce))
print("Temp in F: "+str(w))
print("Humidity: "+str(wea))
