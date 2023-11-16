import requests
from unittest import mock
from unittest.mock import patch, Mock

def test_home(client):
    response = client.get('/')
    assert '<h1  style="color:white; " > This is the Quote Display Service </h1>' in response.get_data(as_text=True)

def test_health(client):
    response = client.get('/health')
    assert 'healthy' == response.text

@patch.object(requests, 'get')
def test_get_quote(mockGet, client):
    mockresponse = Mock()
    mockGet.return_value = mockresponse
    mockresponse.text = 'Awesome quote'
    response = client.get('/get_quote')
    assert 'Awesome quote' in response.get_data(as_text=True)