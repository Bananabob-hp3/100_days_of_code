import os
import requests
from datetime import datetime, timedelta
import json
from twilio.rest import Client

account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

AVS_api_key="HF3PTUC2PFI328VK"
NA_api_key="8dec10e270b74ab4b15fe05d978f64f8"

STOCK_NAME = "TSLA"
COMAPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

params = {
    "symbol":"TSLA",
    "function":"TIME_SERIES_DAILY",
    "apikey":AVS_api_key
}

yesterday = datetime.now().date() - timedelta(days=1)
day_before_yesterday = datetime.now().date() - timedelta(days=2)


response = requests.get(STOCK_ENDPOINT,params=params)
response.raise_for_status()

with open("json_data", "r") as file:
    data = json.load(file)
day_before_yesterday = datetime.now().date() - timedelta(days=2)

yesterday_closing_data = float(data["Time Series (Daily)"][str(yesterday)]["4. close"])
day_before_yesterday_closing_data = float(data["Time Series (Daily)"][str(day_before_yesterday)]["4. close"])

x = abs(yesterday_closing_data - day_before_yesterday_closing_data)

Percentage_Difference = x/int(day_before_yesterday_closing_data) * 100


parameters = {
    "apikey":NA_api_key,
    "qInTitle":"Tesla AND (stock OR shares OR TSLA)",
    "sortBy":"relevancy",
    "language":"en",
    "from":f"{day_before_yesterday}", 
    "to":f"{yesterday}"
}


response = requests.get(NEWS_ENDPOINT, params=parameters)
response.raise_for_status()
data = response.json()

three_articles = data["articles"][:3]

headline = [n["title"]for n in three_articles]
description = [n["description"] for n in three_articles]


if Percentage_Difference > 5:
    client = Client(account_sid, auth_token)
    for single_headline in headline:
        message = client.messages \
            .create(
             body=single_headline,
             from_="+12184504624",
            to="+919557633058"
        ),
    for single_descripton in description:
        message = client.messages \
            .create(
            body=single_descripton,
            from_="+12184504624",
            to="+919557633058"
)

