import requests

url = ''
api_key = 'bcb124d04d41df036dd5ef8e18a45368'

get_weather = True
while get_weather:
    user_input = input("Enter City: ")
    city = user_input
    weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])
    forecast = weather_data.json()['weather'][0]['description']
    feels_like = weather_data.json()['main']['feels_like']
    high = weather_data.json()['main']['temp_max']
    low = weather_data.json()['main']['temp_min']
    humidity = weather_data.json()['main']['humidity']
    if weather == "Clouds":
        weather = "Partly Cloudy"
    print(f"Today in {city}, the weather will be {forecast}.")
    print(f"The temperature is {temp}°F, and it feels like {feels_like:.0f}°F.")
    print(f"The high today is {high:.0f}°F and the low is {low:.0f}°F.")
    print(f"Expect humidity to be at {humidity}.")


    again = input("Would you like to see another city? y/n ")
    if again.lower() != "y":
        get_weather = False
