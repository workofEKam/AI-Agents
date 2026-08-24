from langchain_core.tools import tool
import requests

@tool
def get_current_weather(location: str) -> str:
    """Fetches the current real-time weather. Requires a city name."""
    
    try:
        # Step 1: Convert the city name to latitude and longitude (Geocoding)
        # Weather APIs usually require coordinates, not city names.
        geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={location}&count=1"
        geo_response = requests.get(geo_url)
        geo_data = geo_response.json()
        
        # Guardrail: What if the city doesn't exist?
        if not geo_data.get("results"):
            return f"Error: Could not find the location '{location}'. Ask the user to clarify."
            
        lat = geo_data["results"][0]["latitude"]
        lon = geo_data["results"][0]["longitude"]
        
        # Step 2: Fetch the actual weather using those coordinates
        # (We are requesting the temperature in Celsius, but you can change it to Fahrenheit)
        weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,wind_speed_10m"
        weather_response = requests.get(weather_url)
        weather_data = weather_response.json()
        
        temp = weather_data["current"]["temperature_2m"]
        wind = weather_data["current"]["wind_speed_10m"]
        
        # Return the exact data to the LLM so it can format a nice sentence
        return f"It is currently {temp}°C with a wind speed of {wind} km/h in {location}."
        
    except Exception as e:
        # Guardrail: What if the Open-Meteo servers crash?
        # We return a string back to the LLM so it can apologize to the user.
        return "Error: Weather API is currently unavailable. Apologize to the user and tell them to try again later."