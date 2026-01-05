# I should only put api responses here i think? 

# import openmeteo_requests
# import requests_cache
import requests
# from retry_requests import retry
from config import NEWS_API_KEY, WIKIPEDIA_API_KEY, WIKIPEDIA_USER_AGENT
import datetime
from datetime import datetime, timedelta


dateToday = datetime.today()  # keep as datetime for arithmetic

def weatherAPI():
    # cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
    # retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
    # openmeteo = openmeteo_requests.Client(session = retry_session)

    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": 52.52,
        "longitude": 13.41,
        "current": [
        "temperature_2m",
        "relative_humidity_2m",
        "apparent_temperature",
        "weather_code",
        "wind_speed_10m",
        "precipitation",
        "cloud_cover"
    ],
    }
    weatherResponse = requests.get(url, params=params)
    if weatherResponse.status_code == 200:
        return weatherResponse.json()
    else: 
        return f'error: {weatherResponse.status_code}'

def newsAPI():
    url = 'https://api.worldnewsapi.com/top-news'
    params = {
        'source-country': 'ph',
        'language': 'en',
        'date': (dateToday - timedelta(days=1)).strftime('%Y/%m/%d'),
        "api-key": NEWS_API_KEY,
    }
    newsResponse = requests.get(url, params=params)
    if newsResponse.status_code == 200:
        return newsResponse.json()
    else:
        return f'error: {newsResponse.status_code}'
    
def wikipediaAPI():
    url = 'https://api.wikimedia.org/feed/v1/wikipedia/en/featured/' + dateToday.strftime('%Y/%m/%d')
    headers = {
        'Authorization': WIKIPEDIA_API_KEY,
        'User-Agent': WIKIPEDIA_USER_AGENT
    }
    wikiResponse = requests.get(url, headers=headers)
    if wikiResponse.status_code == 200:
        return wikiResponse.json()
    else:
        return f'error: {wikiResponse.status_code}'



