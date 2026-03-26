import requests
import os

def get_live_weather(location="Bengaluru"):
    """Fetches real-time weather data using WeatherAPI."""
    api_key = os.environ.get("WEATHERAPI_KEY")
    
    if not api_key:
        return f"Simulated Weather for {location}: 33°C, Sunny. (API key not set)."

    # WeatherAPI endpoint
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={location}&aqi=no"
    
    try:
        response = requests.get(url).json()
        
        if "error" in response:
            return f"Weather API Error: {response['error']['message']}"
            
        temp = response["current"]["temp_c"]
        condition = response["current"]["condition"]["text"]
        humidity = response["current"]["humidity"]
        
        return f"Current conditions in {location}: {temp}°C, {condition}, {humidity}% humidity."
    except Exception as e:
        return f"Error fetching weather: {e}"