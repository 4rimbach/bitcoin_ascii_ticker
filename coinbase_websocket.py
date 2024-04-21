from coinbase.websocket import WSClient
import threading
import json

api_key = 'organizations/73f00023-8bb5-4758-ba5e-b63764d95792/apiKeys/ae15b8b0-24c5-409e-844b-46e4f1625981'
api_secret = '' # See the .env file locally

class BitcoinPriceFetcher:
    def __init__(self, api_key, api_secret):
        self.ws_client = WSClient(api_key=api_key, api_secret=api_secret, on_message=self.on_message, verbose=True)
        self.bitcoin_price = None
        self.price_received = threading.Event()

    def on_message(self, msg):
        msg_dict = json.loads(msg)
        if msg_dict['channel'] == 'ticker':
            for event in msg_dict['events']:
                if event['type'] == 'update':
                    for ticker in event['tickers']:
                        if ticker['product_id'] == 'BTC-USD':
                            self.bitcoin_price = ticker['price']
                            self.price_received.set()

    def start(self):
        self.ws_client.open()
        self.ws_client.subscribe(["BTC-USD"], ["ticker"])

    def get_bitcoin_price(self):
        if not self.price_received.is_set():
            self.price_received.wait()
        return self.bitcoin_price


"""
Module testing:

fetcher = BitcoinPriceFetcher(api_key, api_secret)
fetcher.start()

while True:
    print(fetcher.get_bitcoin_price())
    time.sleep(2)
"""
