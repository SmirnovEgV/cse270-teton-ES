import pytest
import requests

def test_get_users_unauthorized(mocker):
    # Mock the requests.get method
    mock_get = mocker.patch("requests.get")
    
    # Define the mocked response for unauthorized access
    mock_response = mocker.Mock()
    mock_response.status_code = 401
    mock_response.text = ""
    mock_get.return_value = mock_response
    
    # Define the URL and parameters
    url = "http://127.0.0.1:8000/users"
    params = {"username": "admin", "password": "admin"}
    
    # Make the GET request
    response = requests.get(url, params=params)
    
    # Assert the response code is 401
    assert response.status_code == 401, f"Expected 401, got {response.status_code}"
    
    # Assert the response body is empty
    assert response.text == "", f"Expected empty response, got: {response.text}"


def test_get_users_authorized(mocker):
    # Mock the requests.get method
    mock_get = mocker.patch("requests.get")
    
    # Define the mocked response for authorized access
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.text = ""
    mock_get.return_value = mock_response
    
    # Define the URL and parameters
    url = "http://127.0.0.1:8000/users"
    params = {"username": "admin", "password": "querty"}
    
    # Make the GET request
    response = requests.get(url, params=params)
    
    # Assert the response code is 200
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    
    # Assert the response body is empty
    assert response.text == "", f"Expected empty response, got: {response.text}"
