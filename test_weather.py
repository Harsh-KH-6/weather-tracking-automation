#!/usr/bin/env python3
"""
Test script for weather logging functionality

This script tests the weather logging system to ensure it works correctly
before setting up the GitHub Actions automation.
"""

import os
import sys
import tempfile
import shutil
from datetime import datetime

# Add the current directory to Python path to import log_weather
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_weather_logging():
    """Test the weather logging functionality."""
    print("🧪 Testing Weather Logging System")
    print("=" * 50)
    
    # Check if API key is available
    api_key = os.getenv('WEATHER_API_KEY')
    if not api_key:
        print("❌ WEATHER_API_KEY environment variable not set")
        print("   Please set it with: export WEATHER_API_KEY='your_api_key'")
        return False
    
    print("✅ API key found")
    
    # Test the log_weather module
    try:
        import log_weather
        print("✅ log_weather module imported successfully")
    except ImportError as e:
        print(f"❌ Failed to import log_weather: {e}")
        return False
    
    # Test API connectivity with a simple request
    try:
        import requests
        test_params = {
            'q': 'Mumbai,IN',
            'appid': api_key,
            'units': 'metric'
        }
        response = requests.get(log_weather.API_BASE_URL, params=test_params, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        if 'main' in data and 'temp' in data['main']:
            print(f"✅ API connectivity test passed - Mumbai temperature: {data['main']['temp']}°C")
        else:
            print("❌ API response format unexpected")
            return False
            
    except Exception as e:
        print(f"❌ API connectivity test failed: {e}")
        return False
    
    # Test CSV creation
    try:
        # Create a temporary directory for testing
        with tempfile.TemporaryDirectory() as temp_dir:
            original_csv = log_weather.CSV_FILE
            test_csv = os.path.join(temp_dir, 'test_weather_log.csv')
            
            # Temporarily change the CSV file path
            log_weather.CSV_FILE = test_csv
            
            # Test CSV creation
            log_weather.create_csv_if_not_exists()
            
            if os.path.exists(test_csv):
                print("✅ CSV file creation test passed")
                
                # Test data writing
                test_data = [{
                    'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    'city': 'Test City',
                    'temperature': 25.0,
                    'weather': 'Clear',
                    'description': 'test weather'
                }]
                
                log_weather.append_weather_data(test_data)
                
                # Verify data was written
                with open(test_csv, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                    if len(lines) >= 2:  # Header + data
                        print("✅ CSV data writing test passed")
                    else:
                        print("❌ CSV data writing test failed")
                        return False
            else:
                print("❌ CSV file creation test failed")
                return False
                
    except Exception as e:
        print(f"❌ CSV testing failed: {e}")
        return False
    
    print("\n🎉 All tests passed! The weather logging system is ready to use.")
    print("\n📋 Next steps:")
    print("1. Push this code to a GitHub repository")
    print("2. Add WEATHER_API_KEY to GitHub Secrets")
    print("3. The GitHub Actions workflow will start automatically")
    
    return True

if __name__ == "__main__":
    success = test_weather_logging()
    sys.exit(0 if success else 1) 