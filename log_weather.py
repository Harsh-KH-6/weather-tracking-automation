#!/usr/bin/env python3
"""
Weather Data Logger for Indian Cities

This script fetches current weather data for multiple Indian cities using the OpenWeatherMap API
and logs the data to a CSV file. It's designed to be run via GitHub Actions for automated
weather tracking and contribution graph updates.

Author: Weather Automation Bot
"""

import os
import csv
import requests
import sys
from datetime import datetime
from typing import Dict, List, Optional

# Configuration
CITIES = [
    {"name": "Mumbai", "country": "IN"},
    {"name": "Hyderabad", "country": "IN"},
    {"name": "Delhi", "country": "IN"},
    {"name": "Chennai", "country": "IN"},
    {"name": "Kolkata", "country": "IN"}
]

CSV_FILE = "weather_log.csv"
API_BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_api_key() -> str:
    """Get the OpenWeatherMap API key from environment variables."""
    api_key = os.getenv('WEATHER_API_KEY')
    if not api_key:
        raise ValueError("WEATHER_API_KEY environment variable is not set")
    return api_key

def fetch_weather_data(city: str, country: str, api_key: str) -> Optional[Dict]:
    """
    Fetch weather data for a specific city using the OpenWeatherMap API.

    Args:
        city: City name
        country: Country code (e.g., 'IN' for India)
        api_key: OpenWeatherMap API key

    Returns:
        Dictionary containing weather data or None if request fails
    """
    try:
        params = {
            'q': f"{city},{country}",
            'appid': api_key,
            'units': 'metric'  # Use metric units (Celsius)
        }

        response = requests.get(API_BASE_URL, params=params, timeout=10)
        response.raise_for_status()

        data = response.json()

        # Extract relevant weather information
        weather_info = {
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'city': city,
            'temperature': data['main']['temp'],
            'weather': data['weather'][0]['main'],
            'description': data['weather'][0]['description']
        }

        print(f"✅ Successfully fetched weather data for {city}")
        return weather_info

    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching weather data for {city}: {e}")
        return None
    except (KeyError, IndexError) as e:
        print(f"❌ Error parsing weather data for {city}: {e}")
        return None

def create_csv_if_not_exists():
    """Create the CSV file with headers if it doesn't exist."""
    if not os.path.exists(CSV_FILE):
        headers = ['timestamp', 'city', 'temperature', 'weather', 'description']
        with open(CSV_FILE, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
        print(f"📄 Created new CSV file: {CSV_FILE}")

def append_weather_data(weather_data: List[Dict]):
    """Append weather data to the CSV file."""
    headers = ['timestamp', 'city', 'temperature', 'weather', 'description']

    with open(CSV_FILE, 'a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writerows(weather_data)

    print(f"📝 Appended {len(weather_data)} weather records to {CSV_FILE}")

def main():
    """Main function to orchestrate the weather logging process."""
    print("🌤️  Starting weather data collection...")
    print(f"📅 Current time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    try:
        # Get API key
        api_key = get_api_key()
        print("🔑 API key loaded successfully")

        # Create CSV file if it doesn't exist
        create_csv_if_not_exists()

        # Collect weather data for all cities
        weather_data = []
        successful_fetches = 0

        for city_info in CITIES:
            city_name = city_info['name']
            country_code = city_info['country']

            print(f"🌍 Fetching weather data for {city_name}...")
            weather_info = fetch_weather_data(city_name, country_code, api_key)

            if weather_info:
                weather_data.append(weather_info)
                successful_fetches += 1
            else:
                print(f"⚠️  Skipping {city_name} due to fetch error")

        # Append data to CSV if we have any successful fetches
        if weather_data:
            append_weather_data(weather_data)
            print(f"🎉 Successfully logged weather data for {successful_fetches}/{len(CITIES)} cities")
        else:
            print("❌ No weather data was successfully fetched")
            sys.exit(1)

    except ValueError as e:
        print(f"❌ Configuration error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()