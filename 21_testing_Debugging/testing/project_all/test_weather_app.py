import pytest
from weather_app import get_weather_data

# Apnar OpenWeatherMap API key ekhane use korun
API_KEY = "5a68f249fd2cd34161ebdfb432ddd41f"

def test_valid_city():
    """
    Valid city er jonno successful API response check kore.
    """
    response = get_weather_data("Dhaka", API_KEY)
    assert response is not None
    assert response['cod'] == 200

def test_invalid_city():
    """
    Invalid city er jonno 404 error check kore.
    """
    response = get_weather_data("xyz_city_123", API_KEY)
    assert response is  None
    # assert response['cod'] == '404'

def test_empty_city():
    """
    Empty string input er jonno 404 error check kore.
    """
    response = get_weather_data("", API_KEY)
    assert response is  None
    assert response['cod'] == '404'

def test_invalid_api_key():
    """
    Invalid API key diye try korle ki hoy sheta check kore.
    """
    response = get_weather_data("London", "invalid_key")
    assert response is not None
    assert response['cod'] == 401
    assert response['message'] == "Invalid API key. Please see https://openweathermap.org/faq#errors for more info."