import requests
def weather_today():
    city = "Moscow,RU"
    appid = "3f110f6a83f5e05f9253f77c14eb0c47"

    res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                       params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
    data = res.json()

    text_weather = f"Город: {city}, " \
                   f"\nПогодные условия: {data['weather'][0]['description']} " \
                   f"\nТемпература: {data['main']['temp']} " \
                   f"\nМинимальная температура: {data['main']['temp_min']} " \
                   f"\nМаксимальная температура: {data['main']['temp_max']} " \
                   f"\nВетер: {data['wind']['speed']} " \
                   f"\nВидимость: {data['visibility']}"
    return text_weather
def dog_picture_url():
    res = requests.get("https://random.dog/woof.json")
    temp_res = res.json()
    dog_url = temp_res['url']
    return dog_url
def my_ip():
    res = requests.get("https://api.ipify.org?format=json")
    ip = res.json()
    return ip['ip']
