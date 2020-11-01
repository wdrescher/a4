import requests
import pytest
from flask.json import jsonify

def test_shuffle(): 
    original_list = [1,2,3,4]
    payload = {
        "list_of_ints": original_list
    }
    response = requests.request(method="GET", url="http://localhost:5000/shuffle/", json=payload)
    if response.status_code == 200: 
        response_data = response.json()
        shuffled_list = response_data["shuffled_list"]
        assert shuffled_list != original_list
    else: 
        assert False

if __name__ == "__main__": 
    test_shuffle()