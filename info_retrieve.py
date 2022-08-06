import requests

class retrieve_api:
    def __init__(self, city_name, state_name):
        self.city_name = city_name
        self.state_name = state_name
        self.API_KEY = "2b2bc47db728fbe9d893a43e654f0903"
        self.api_url = "https://api.openweathermap.org/data/2.5/weather?q={0},{1}&appid={2}".format(self.city_name, self.state_name, self.API_KEY)
        self.weather_api = requests.get(self.api_url).json()

        
    def get_icon(self):
        return "http://openweathermap.org/img/wn/{0}@2x.png".format(self.weather_api["weather"][0]["icon"])

    def get_weather_temp_fah(self):
        weather_temp = self.weather_api["main"]["temp"]
        return round((weather_temp - 273.15) * (9 / 5.0) + 32, 2)
    
    def get_weather_temp_cel(self):
        weather_temp = self.weather_api["main"]["temp"]
        return "Temperature: {0} celcius".format(round(weather_temp - 273.15, 2))
        
    
    def get_weather_description(self):
        return "Weather Description: {0}".format(self.weather_api["weather"][0]["description"])
    
    def feels_like_fah(self):
        feels_like = self.weather_api["main"]["feels_like"]
        feels_like_fah = (feels_like - 273.15) * (9 / 5.0) + 32
        return round(feels_like_fah, 2)
    
    def feels_like_cel(self):
        feels_like = self.weather_api["main"]["feels_like"]
        feels_like_cel = feels_like - 273.15
        return "The weather today feels like: {0}".format(feels_like_cel)
    
    def weather_humidity(self):
        weather_humidity = self.weather_api["main"]["humidity"]
        return "Humidity: {0}".format(weather_humidity)
    
    def temp_min_fah(self):
        temp_min = self.weather_api["main"]["temp_min"]
        temp_min_fah = (temp_min - 273.15) * (9 / 5.0) + 32
        return round(temp_min_fah, 2)
    
    def temp_min_cel(self):
        temp_min = self.weather_api["main"]["temp_min"]
        temp_min_cel = temp_min - 273.15
        return "Lowest Temperature: {0}".format(temp_min_cel)
    
    def temp_max_fah(self):
        temp_max = self.weather_api["main"]["temp_max"]
        temp_max_fah = (temp_max - 273.15) * (9 / 5.0) + 32
        return round(temp_max_fah, 2)
    
    def temp_max_cel(self):
        temp_max = self.weather_api["main"]["temp_max"]
        temp_max_cel = temp_max - 273.15
        return "Highest Temperature: {0}".format(temp_max_cel)



if __name__ == "__main__":
    # Testing
    city = input("City Name: ")
    state = input("State Name: ")
    API_KEY = "2b2bc47db728fbe9d893a43e654f0903"
    test = retrieve_api(city, state)

    print("-------------------{0}, {1} Weather Result-------------------".format(city, state))
    print("Temperature: {0}".format(test.get_weather_temp_cel()))
    print("Humidity: {0}".format(test.weather_humidity()))
    print("The weather today feels like: {0}".format(test.feels_like_cel()))
    print("Lowest Temperature: {0}".format(test.temp_min_cel()))
    print("Highest Temperature: {0}".format(test.temp_max_cel()))
    print("Weather Description: {0}".format(test.get_weather_description()))
    print("\nEnd of Searching")
