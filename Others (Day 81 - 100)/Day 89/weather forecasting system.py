'''
    - Write a program to create a class that represents a weather forecasting system with 
      methods to add, remove, and display weather data.
'''

class WeatherData:
    def __init__(self, location, temperature, humidity, wind_speed, forecast):
        self.location = location
        self.temperature = temperature
        self.humidity = humidity
        self.wind_speed = wind_speed
        self.forecast = forecast

    def __str__(self):
        return f"Weather in {self.location}:\nTemperature: {self.temperature}°C\nHumidity: {self.humidity}%\nWind Speed: {self.wind_speed} km/h\nForecast: {self.forecast}"


class WeatherForecastingSystem:
    def __init__(self):
        self.weather_data = {}

    def add_weather_data(self, location, temperature, humidity, wind_speed, forecast):
        self.weather_data[location] = WeatherData(location, temperature, humidity, wind_speed, forecast)
        print(f"Weather data added for {location}")

    def remove_weather_data(self, location):
        if location in self.weather_data:
            del self.weather_data[location]
            print(f"Weather data removed for {location}")
        else:
            print(f"Weather data not found for {location}")

    def display_weather_data(self, location=None):
        if location:
            if location in self.weather_data:
                print(self.weather_data[location])
            else:
                print(f"Weather data not found for {location}")
        else:
            for location, data in self.weather_data.items():
                print(data)
                print("--------------------")

    def update_weather_data(self, location, temperature=None, humidity=None, wind_speed=None, forecast=None):
        if location in self.weather_data:
            if temperature:
                self.weather_data[location].temperature = temperature
            if humidity:
                self.weather_data[location].humidity = humidity
            if wind_speed:
                self.weather_data[location].wind_speed = wind_speed
            if forecast:
                self.weather_data[location].forecast = forecast
            print(f"Weather data updated for {location}")
        else:
            print(f"Weather data not found for {location}")


# Example usage
weather_system = WeatherForecastingSystem()

while True:
    print("\nWeather Forecasting System")
    print("1. Add weather data")
    print("2. Remove weather data")
    print("3. Display weather data")
    print("4. Update weather data")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        location = input("Enter location: ")
        temperature = float(input("Enter temperature (°C): "))
        humidity = float(input("Enter humidity (%): "))
        wind_speed = float(input("Enter wind speed (km/h): "))
        forecast = input("Enter forecast: ")
        weather_system.add_weather_data(location, temperature, humidity, wind_speed, forecast)
    elif choice == "2":
        location = input("Enter location: ")
        weather_system.remove_weather_data(location)
    elif choice == "3":
        location = input("Enter location (or leave blank for all): ")
        if location:
            weather_system.display_weather_data(location)
        else:
            weather_system.display_weather_data()
    elif choice == "4":
        location = input("Enter location: ")
        temperature = input("Enter new temperature (°C) (or leave blank): ")
        humidity = input("Enter new humidity (%) (or leave blank): ")
        wind_speed = input("Enter new wind speed (km/h) (or leave blank): ")
        forecast = input("Enter new forecast (or leave blank): ")
        temperature = float(temperature) if temperature else None
        humidity = float(humidity) if humidity else None
        wind_speed = float(wind_speed) if wind_speed else None
        weather_system.update_weather_data(location, temperature, humidity, wind_speed, forecast)
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")