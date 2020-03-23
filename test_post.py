# Simple script that sends GET request to URL endpoint to get all feeds for test page
import requests
import pytest


def test_get_request():
    url = "https://graph.facebook.com/v6.0/108928174075398/feed?access_token=EAAC9ZBqHFFUYBAJ4cwt2muwqTYO47n3ZAJOcgYwpSEX6Pan92RGkPVhZAga4diUc7vNR4ZBCqZAzLPIZCLAbc2KKhvBldbnfyblQi0EBKy98xypjzHjv9ipXoqdsk9YkClgF3BhIhM7wrByehWHyfjIUV4ASKLMo1dHXZCegmyn6s0lR73X4k6MnKdm2WvfU1TYNZBZAjB52axBjqDT9UMzdT"
    payload = {}
    headers= {}

    # Sends GET request
    response = requests.request("GET", url, headers=headers, data = payload)
    # print(response)

    # Asserts 200 response code
    assert response.status_code == 200