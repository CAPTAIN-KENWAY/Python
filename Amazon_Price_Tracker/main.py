import smtplib
from bs4 import BeautifulSoup
import requests
import locale

locale.setlocale(locale.LC_ALL, '')
EMAIL = "pythontesting810@gmail.com"
PASSWORD = "jflzmvkrbbuhavxz"
URL = "https://www.amazon.in/dp/B082H2R32N?ref_=cm_sw_r_cp_ud_dp_R726M0NHA50WXD0BX7H2"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    "Accept-Language": "en,en-GB;q=0.9"
}
response = requests.get(url=URL, headers=headers)
soup = BeautifulSoup(response.text, "lxml")
search_price = soup.find(name="span", class_="a-offscreen")
price = locale.atof(search_price.text[1:])
product = soup.find(name="span", id="productTitle")
product_title = product.text.strip()

if price < 1000:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr="EMAIL",
            to_addrs="guptakaran094948@gmail.com",
            msg=f"Subject: Amazon Price Alert!\n\n{product_title} is now {search_price.text}.\n{URL}".encode("utf-8")
        )
