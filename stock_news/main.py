import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

alpha_api = "alphavantage API"
news_api = "newsapi API"

account_sid = "Twilio account sid"
auth_token = "Twilio auth token"

alpha_params = {"function": "TIME_SERIES_DAILY", "symbol": STOCK_NAME, "apikey": alpha_api, "datatype": "json"}

stock_response = requests.get(url=STOCK_ENDPOINT, params=alpha_params)
data = stock_response.json()["Time Series (Daily)"]
# print(data["Time Series (Daily)"]["2021-10-15"])
 
data_list = [value for key, value in data.items()]
yesterday_stock_price = float(data_list[0]["4. close"])
print(yesterday_stock_price)

# Get the day before yesterday's closing stock price

before_yesterday_stock_price = float(data_list[1]["4. close"])
print(before_yesterday_stock_price)

# difference = abs(round(yesterday_stock_price - before_yesterday_stock_price, 4))
difference = yesterday_stock_price - before_yesterday_stock_price
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

# Work out the percentage difference in price between closing price yesterday and closing price the day
# before yesterday.

percentage_diff = round((difference / yesterday_stock_price) * 100)
print(percentage_diff)

if percentage_diff >= 5:
    # Use the News API to get articles related to the COMPANY_NAME.

    news_params = {
        "qInTitle": COMPANY_NAME, "apiKey": news_api, "language": "en"
    }
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]

    ##https://newsapi.org/
    # Get the first 3 news pieces for the COMPANY_NAME.
    # Use Python slice operator to create a list that contains the first 3 articles.
    # https://stackoverflow.com/questions/509211/understanding-slice-notation

    three_articles = articles[:3]

    ## Use twilio.com/docs/sms/quickstart/python
    # to send a separate message with each article's title and description to your phone number. 

# Create a new list of the first 3 article's headline and description.

    formatted_articles = [f'{STOCK_NAME}: {up_down}{percentage_diff}%\n' \
                          f'Headline: {i["title"]}. \nBrief: {i["description"]}' for i in three_articles]
    print(formatted_articles[0])

# Send each article as a separate message via Twilio.

    client = Client(account_sid, auth_token)

    for article in formatted_articles:
        message = client.messages \
                        .create(
                             body=article,
                             from_='Your Twilio Phone number',
                             to='Phone number you want to be sent to'
                         )


# Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required 
to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the 
height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to 
file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height 
of the coronavirus market crash.
"""

