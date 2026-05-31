import os
import requests
from datetime import datetime

time_now = datetime(year=2026, month=5, day=29)
day_now = time_now.strftime("%Y%m%d")

PIXELA_ENDPOINT = "https://pixe.la/v1/users"

USERNAME = "melatonin"

GRAPH_ID = "graph1"

user_params = {
    "token": os.environ.get("PIXELA_TOKEN"),
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}

response = requests.post(url=PIXELA_ENDPOINT, json=user_params)

GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

graph_config = {
    "id":GRAPH_ID,
    "name":"Coding Graph",
    "unit":"Pixelian hour",
    "type":"float",
    "color":"ajisai"
}

headers = {
    "X-USER-TOKEN": user_params["token"]
}

response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=headers)


PIXAL_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"

headers = {
    "X-USER-TOKEN": user_params["token"]
}

pixal_config = {
    "date":day_now,
    "quantity":"11"
}

response = requests.post(PIXAL_ENDPOINT, json=pixal_config, headers=headers)

CURL_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{day_now}"

headers = {
    "X-USER-TOKEN": user_params["token"]
}

curl_config = {
    "quantity":"7"
}

response = requests.put(CURL_ENDPOINT, json=curl_config, headers=headers)


DELETE_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{day_now}"

response = requests.delete(DELETE_ENDPOINT, headers=headers)
print(response.text)
