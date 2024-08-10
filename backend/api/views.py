from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import requests

def get_soil_properties(lat, lon):
      pass
def get_weather_info(q, api_key):
    """Fetches weather information from a weather API (replace with your preferred API)"""
    base_url = "http://api.weatherapi.com/v1/current.json"  # Replace with your weather API URL
    params = {"key": api_key,"q":q}

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an exception for error HTTP statuses
        data = json.loads(response.text)
        # Extract desired weather data (temperature, humidity, rainfall)
        return {
            "temperature": data["current"]["temp_c"],
            "humidity": data["current"]["humidity"],
            "rainfall": data["current"]["precip_mm"]  # Replace with appropriate rainfall data
        }
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return {}
def get_combined_data(key,q):
    loc=51
    lat=139
    soil_data = get_soil_properties(loc,lat)
    weather_data = get_weather_info(key,q)
    combined_data=weather_data
    js=[58,18.5,2,weather_data['temperature'],weather_data['humidity'],7.7,weather_data['rainfall']]
    print(js)
    print(type(combined_data))
    process_data_for_value(js)
    # combined_data = {**soil_data, **weather_data}
    return combined_data

@csrf_exempt
def handle_form_data(request):
  if request.method == 'POST':
    json_data = json.loads(request.body)
    print(json_data)
    latitude_data=json_data['latitude']
    longitude_data=json_data['longitude']
    
    # Access form data using data['field1'], data['field2'], 
    return JsonResponse(data=json_data)
  return JsonResponse({'error':'Only POST request are allowed'},status=400)

def format_lat_lng(latitude, longitude):
  """Formats latitude and longitude as a query parameter."""
  return f"{latitude:6f},{longitude:6f}"

def process_data_for_value(data):
  base_url="http://52.4.151.236:8501"
  if data is not None:
    response=requests.post(base_url,data)
    response.raise_for_status()  # Raise an exception for error HTTP statuses
    data = json.loads(response.text)
    return JsonResponse(data=data,status=200)
  return JsonResponse({'error':"The data from API's is None"},status=400)
latitude = 51
longitude = 139
weather_api_key ="697b9bd9f160492881a10748241008"
q=format_lat_lng(latitude,longitude)
result = get_combined_data(q,weather_api_key)
print(result)
