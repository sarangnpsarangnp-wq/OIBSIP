# Python Weather Application

## 1. Project Overview

The Python Weather Application is a simple command-line application developed using Python. It retrieves real-time weather information for a user-specified city using the OpenWeatherMap API.

The application displays important weather details such as temperature, humidity, weather conditions, and wind speed.

## 2. Objective

The main objective of this project is to develop a Python application that fetches and displays real-time weather information using an external weather API.

It also helps in understanding API integration, JSON data handling, Python functions, and exception handling.

## 3. Technologies Used

* **Programming Language:** Python
* **Code Editor:** Visual Studio Code
* **Library:** Requests
* **API:** OpenWeatherMap Current Weather API
* **Data Format:** JSON

## 4. Features

The application includes the following features:

1. Accepts a city name from the user.
2. Fetches real-time weather information.
3. Displays temperature in Celsius.
4. Converts and displays temperature in Fahrenheit.
5. Displays humidity percentage.
6. Shows the current weather description.
7. Displays wind speed.
8. Handles invalid city names.
9. Handles network connection errors and request timeouts.
10. Allows users to check the weather of multiple cities.

## 5. Project Structure

```text
Weather_App/
│
├── weather_app.py
├── README.md
│
└── Screenshots/
    ├── weather_output.png
    ├── invalid_city.png
    └── error_handling.png
```

## 6. Installation Requirements

The following software and libraries are required:

* Python 3
* Visual Studio Code
* Requests library
* OpenWeatherMap API Key

Install the Requests library using:

```bash
pip install requests
```

## 7. API Configuration

This project uses the OpenWeatherMap Current Weather API to retrieve live weather information.

Steps to configure the API:

1. Visit https://openweathermap.org/
2. Create a free account.
3. Generate an API key.
4. Add the API key to the Python application.

Keep the API key private and do not upload it publicly.

## 8. How to Run the Project

1. Open the Weather_App folder in Visual Studio Code.
2. Open the terminal.
3. Install the required Requests library.
4. Configure the OpenWeatherMap API key.
5. Execute the following command:

```bash
python weather_app.py
```

6. Enter the city name when prompted.
7. The application displays the current weather information.

## 9. Sample Output

```text
====================================
       PYTHON WEATHER APP
====================================

Enter city name: Bangalore

========== WEATHER REPORT ==========
City: Bangalore
Temperature: 27.5 °C
Temperature: 81.5 °F
Humidity: 65 %
Weather: Scattered Clouds
Wind Speed: 3.5 m/s
====================================

Check another city? (yes/no):
```

Note: The above values are sample output. Actual weather information changes according to live API data.

## 10. Error Handling

The application handles different errors:

* Empty city input: Displays a message asking the user to enter a city.
* Invalid city: Displays a city not found message.
* Invalid API key: Displays an API authentication error.
* Network timeout: Displays a timeout message.
* Internet connection failure: Displays a connection error.

## 11. Learning Outcomes

Through this project, I learned:

* Python programming and functions.
* Installing and using external Python libraries.
* Making API requests using the Requests library.
* Retrieving and processing JSON data.
* Handling exceptions in Python.
* Displaying real-time information through an API.

## 12. Conclusion

The Python Weather Application successfully demonstrates how Python can be integrated with an external API to retrieve real-time weather information.

This project improved my understanding of Python programming, API integration, JSON processing, and error handling. It provided practical experience in developing a real-world Python application.
