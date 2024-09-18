import requests

def get_weather(city):
    api_key = '46bec201377b3ea55a754ae1e8202c68'  # Replace with your OpenWeatherMap API key
    base_url = 'http://api.openweathermap.org/data/2.5/weather?q=CITY_NAME&appid=YOUR_API_KEY&units=metric'
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }

    try:
        # Make the API request
        response = requests.get(base_url, params=params)
        # Output the full URL for debugging
        print(f"Request URL: {response.url}")
        response.raise_for_status()  # Raise an exception for HTTP errors

        data = response.json()
        main = data['main']
        weather_desc = data['weather'][0]['description']
        temp = main['temp']
        humidity = main['humidity']
        pressure = main['pressure']

        weather_info = f"Weather in {city}:\n" \
                       f"Temperature: {temp}°C\n" \
                       f"Description: {weather_desc.capitalize()}\n" \
                       f"Humidity: {humidity}%\n" \
                       f"Pressure: {pressure} hPa"

        return weather_info

    except requests.exceptions.HTTPError as http_err:
        return f"HTTP error occurred: {http_err} - {response.text}"
    except requests.exceptions.RequestException as req_err:
        return f"Request error occurred: {req_err}"
    except KeyError:
        return "Error: Could not find weather information for the given city."
    except Exception as e:
        return f"An error occurred: {e}"

# Example usage:
if __name__ == "__main__":
    city_name = input("Enter city name: ")
    print(get_weather(city_name))