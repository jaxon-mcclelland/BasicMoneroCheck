import requests
import json
import time


token = [YOUR TELEGRAM API TOKEN HERE]
url = f"https://api.telegram.org/bot{token}/sendMessage"

r = requests.get('https://api.cryptowat.ch/markets/kraken/xmrusd/summary').json()
price = (f"{r['result']['price']['last']}")

output = "The Current Price of Monero is $" + price 



data = {'chat_id': '850691491', 'text': output}
requests.post(url, data).json()