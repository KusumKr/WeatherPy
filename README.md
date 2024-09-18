# WeatherPy
WeatherPy is a simple Python application that fetches the current weather information for any city using the OpenWeatherMap API.

## Features
- Fetches real-time weather data.
- Displays temperature, weather description, humidity, and pressure.
- Simple and easy-to-use command-line interface.

## Prerequisites
- Python 3.x
- An API key from [OpenWeatherMap](https://openweathermap.org/api)
- `requests` library (install using `pip` if not already installed)

## Installation
1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/WeatherNow.git
    cd WeatherNow
    ```
2. **Install dependencies**:
    ```bash
    pip install requests
    ```
## Troubleshooting
- **Invalid API Key**: If you encounter a "401 Unauthorized" error, double-check your API key.
- **City Not Found**: If you receive a "404 Not Found" error, ensure that the city name is spelled correctly.
- **Request Limit Exceeded**: Free OpenWeatherMap API keys have a request limit. If you exceed this limit, you may need to wait or upgrade your plan.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request if you'd like to contribute.

## Acknowledgments
- Thanks to [OpenWeatherMap](https://openweathermap.org/) for providing the weather API.    
    

## Usage
1. **Obtain an API Key**:
   - Sign up at [OpenWeatherMap](https://openweathermap.org/) and generate a free API key.
   
2. **Replace the API Key in the Code**:
   - Open `weather_app.py` and replace `'YOUR_API_KEY'` with your actual API key.

3. **Run the Application**:
    ```bash
    python weather_app.py
    ```
4. **Enter the City Name**:
   - When prompted, enter the name of the city you want to check the weather for.
