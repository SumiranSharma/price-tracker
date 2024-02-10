import requests #accessing URL and pull out he actual data
from bs4 import BeautifulSoup #parse and pulls individual items from it
import smtplib  #standard protocol for sending email msgs 

URL = 'https://www.amazon.in/Sony-PS5-PlayStation-Console/dp/B0BRCP72X8/ref=sr_1_3?crid=23EEQBEN6FQ3H&keywords=ps5&qid=1707545306&sprefix=ps%2Caps%2C230&sr=8-3'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'}
#gives information about browser

def check_price():
    page = requests.get(URL, headers=headers)
    #returns all the data from the website

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    gettingPrice = soup.find('span', class_='a-price-whole').get_text()
    price = gettingPrice.replace(',', '')
    #cant compare string to number so converting
    converted_price = float(price[0:6])

    if(converted_price < 50000):
        send_mail()

    print(converted_price)
    print(title.strip())

    #(original code)
    #if(converted_price < 50000):  
    #   send_mail() 

    #(trail code)
    if(converted_price > 50000):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo() #email client to identify itself to an email server
    server.starttls() #encrypts connection
    server.ehlo()

    server.login ('dakshftw01@gmail.com', 'ndkc jjeq spbh tzuh')
    #server.login('sumiran@gmail.com', 'password-from-google_app_password')

    subject = 'price low get it now!'
    body = 'Check the Product- https://www.amazon.in/Sony-PS5-PlayStation-Console/dp/B0BRCP72X8/ref=sr_1_3?crid=23EEQBEN6FQ3H&keywords=ps5&qid=1707545306&sprefix=ps%2Caps%2C230&sr=8-3'
    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'dakshftw01@gmail.com',
        'sumiran.s.0222@inspiria.edu.in',
        msg
    )
    print('HEY EMAIL HAS BEEN SENT')

    server.quit()

check_price()