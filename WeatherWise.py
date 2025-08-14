import requests

API_KEY = "8ce3c94c9c9c6b3bfc2c8064ab950a68"  
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city_name):
    url = f"{BASE_URL}?q={city_name}&appid={API_KEY}&units=metric"
    
    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        
        # Corrected cod check
        if response.status_code == 200 and int(data.get("cod", 0)) == 200:
            main = data["main"]
            weather = data["weather"][0]
            sys = data["sys"]
            
            print(f"\nWeather in {data['name']}, {sys['country']}:")
            print(f"Description   : {weather['description'].capitalize()}")
            print(f"Temperature   : {main['temp']}°C")
            print(f"Feels Like    : {main['feels_like']}°C")
            print(f"Min Temp      : {main['temp_min']}°C")
            print(f"Max Temp      : {main['temp_max']}°C")
            print(f"Pressure      : {main['pressure']} hPa")
            print(f"Humidity      : {main['humidity']}%\n")
        else:
            print(f"City '{city_name}' not found. Please check spelling.")
            
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to OpenWeather API: {e}")

if __name__ == "__main__":
    city_name = input("Enter city name: ").strip()
    get_weather(city_name)
    input("Press Enter to exit...")

