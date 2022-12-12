from email import message
import requests
import smtplib
import datetime as dt

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API = "FLHNZHRUI31VPGUJ"
NEWS_API = "588c17f34504425ab1137d9e3d68b217"
EMAIL = "pythontesting810@gmail.com"
PASSWORD = "jflzmvkrbbuhavxz"


# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

# STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
def send_email(symbol, percent, message):
    msg=f"Subject:Stock News Alert!\n\nTSLA: {symbol}{abs(percent)}%\n\n{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs="shivamsaini948@gmail.com",
            msg=msg.encode('utf-8')
        )

def get_news():
    message = ""
    news_response = requests.get(url="https://newsapi.org/v2/everything", params=news_parameters)
    news_response.raise_for_status()
    news_data = news_response.json()
    top_news = news_data["articles"][0:3]
    for i in top_news:
        message = message + f"Headline: {i['title']} \nBrief: {i['description']} \n\n"
    return message

today = str(dt.date.today())

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API,
    "outputsize": "compact"
}

news_parameters = {
    'q': COMPANY_NAME,
    'apiKey': NEWS_API
}
stock_response = requests.get(url="https://www.alphavantage.co/query", params=stock_parameters)
stock_response.raise_for_status()
stock_data = stock_response.json()

closing_data = [float(value["4. close"])
                for key, value in stock_data["Time Series (Daily)"].items()]
change = (closing_data[0]-closing_data[1])/closing_data[0]*100
change = round(change, 2)
if  change >= 2: 
    send_email("🔺", change, get_news())  
elif change <= -2:
    send_email("🔻", change, get_news())

