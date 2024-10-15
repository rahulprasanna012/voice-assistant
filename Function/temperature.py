import requests
import json
from Base.Mouth import *  # Assuming this is a custom module for the `speak` function.


def get_temperature_openweathermap(city):
    api_key = "57750a40690b5a50f53cc755c386cfbc"  # Replace with your actual OpenWeatherMap API key
    endpoint = "http://api.openweathermap.org/data/2.5/weather"

    # Send GET request to API endpoint
    response = requests.get(endpoint, params={"q": city, "appid": api_key, "units": "metric"})

    # Check if the request was successful
    if response.status_code == 200:
        # Parse JSON response
        data = json.loads(response.text)

        # Check if 'main' key is present
        if 'main' in data:
            # Extract temperature in Celsius
            temperature_celsius = data["main"]["temp"]
            return temperature_celsius
        else:
            print("Error: 'main' key not found in API response")
    else:
        print(f"Error: Failed to fetch data from API. Status code: {response.status_code}")

    return None


def get_city_from_ip():
    """Get the user's city based on their IP address using ipapi.co."""
    try:
        response = requests.get('https://ipapi.co/json/')
        if response.status_code == 200:
            location_data = response.json()
            city = location_data.get('city')
            if city:
                return city
            else:
                print("Error: Could not detect city from IP address.")
        else:
            print(f"Error: Failed to get location. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred while getting the location: {e}")

    return None


def Temp():
    # Automatically get the user's current city using IP-based location
    city = get_city_from_ip()

    if city:
        # Get temperature using OpenWeatherMap API
        temperature_celsius = get_temperature_openweathermap(city)

        if temperature_celsius is not None:
            speak(f"The weather in {city} is {temperature_celsius}°C")
        else:
            speak("Temperature data not available.")
    else:
        speak("Unable to detect your location.")



