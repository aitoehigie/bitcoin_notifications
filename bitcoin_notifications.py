import requests
import ujson as json
import time
from datetime import datetime

BITCOIN_API_URL = "https://api.coinmarketcap.com/v1/ticker/bitcoin/"
IFTTT_WEBHOOKS_URL = "https://maker.ifttt.com/trigger/{}/with/key/c2ZxtFZhCojT44CnLMUkCL"

def get_latest_bitcoin_price():
    response = requests.get(BITCOIN_API_URL)
    response_json = json.loads(response.content or response.text)
    return float(response_json[0].get("price_usd")

def post_ifttt_webhook(event, value):
    # The payload that will be sent to IFTTT service
    payload = dict(value1 = value)
    # inserts our desired event
    ifttt_event_url = IFTTT_WEBHOOKS_URL.format(event)
    # send a HTTP POST request to the webhook URL
    requests.post(ifttt_event_url, json=payload)

def main():
    pass


if __name__ == "__main__":
    main()


