import requests

# Enter your OpenWeatherMap API key
API_KEY = "298da47ffaf8d94c514e55f2bb6b8891"


def get_weather(city):

    if not city.strip():
        print("Please enter a city name!")
        return

    # API URL
    url = "https://api.openweathermap.org/data/2.5/weather"

    # Request parameters
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        # Send request to weather API
        response = requests.get(url, params=params, timeout=10)

        if response.status_code == 200:

            data = response.json()

            # Extract weather details
            city_name = data["name"]
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            description = data["weather"][0]["description"]
            wind_speed = data["wind"]["speed"]

            # Convert Celsius to Fahrenheit
            fahrenheit = (temperature * 9/5) + 32

            # Display weather information
            print("\n========== WEATHER REPORT ==========")
            print("City:", city_name)
            print("Temperature:", temperature, "°C")
            print("Temperature:", round(fahrenheit, 2), "°F")
            print("Humidity:", humidity, "%")
            print("Weather:", description.title())
            print("Wind Speed:", wind_speed, "m/s")
            print("====================================")

        elif response.status_code == 404:
            print("City not found! Please enter a valid city.")

        elif response.status_code == 401:
            print("Invalid API key or API key not activated.")

        else:
            print("Unable to fetch weather information.")

    except requests.exceptions.Timeout:
        print("Network timeout! Please try again.")

    except requests.exceptions.ConnectionError:
        print("Please check your internet connection.")

    except requests.exceptions.RequestException as e:
        print("Error:", e)


# Main program
print("====================================")
print("       PYTHON WEATHER APP")
print("====================================")

while True:

    city = input("\nEnter city name: ")

    get_weather(city)

    choice = input("\nCheck another city? (yes/no): ")

    if choice.lower() != "yes":
        print("\nThank you for using Weather App!")
        break