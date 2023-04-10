import base64
import datetime
import hashlib
import hmac
import json
import requests
import numpy as np
import time
import random


API_KEY = "YOUR-API-KEY"
SECRET_KEY = "YOUR-SECRET-KEY"
PASSPHRASE = "YOUR-PASSPHRASE"

COLD_WALLET_ADDRESSES = [
    "0x000...000",
    "0x000...000",
    "0x000...000",
    # Add more addresses here
]

BASE_URL = "https://www.okx.com"


def get_headers(api_key, secret_key, passphrase, method, request_path, body):
    timestamp = datetime.datetime.utcnow().isoformat(timespec="seconds") + "Z"
    message = "".join([timestamp, method, request_path, body or ""])

    signature = hmac.new(bytes(secret_key, "utf-8"), bytes(message, "utf-8"), hashlib.sha256)
    signature_b64 = base64.b64encode(signature.digest()).decode("utf-8")

    headers = {
        "Content-Type": "application/json",
        "OK-ACCESS-KEY": api_key,
        "OK-ACCESS-SIGN": signature_b64,
        "OK-ACCESS-TIMESTAMP": timestamp,
        "OK-ACCESS-PASSPHRASE": passphrase,
    }

    return headers


def withdraw_funds_to_cold_wallets(wallet_addresses):
    request_path = "/api/v5/asset/withdrawal"
    method = "POST"

    for address in wallet_addresses:
        token = "ETH"
        chain = "ETH-Arbitrum one"
        min_amount = 0.1
        max_amount = 0.2345
        decimal_places = random.randint(5, 8)
        amount = round(np.random.uniform(min_amount, max_amount), decimal_places)

        payload = {
            "ccy": token,
            "amt": "{:.8f}".format(amount),
            "dest": "4",
            "toAddr": address,
            "fee": "0.0001",
            "chain": chain,
        }

        headers = get_headers(API_KEY, SECRET_KEY, PASSPHRASE, method, request_path, json.dumps(payload))

        response = requests.post(BASE_URL + request_path, headers=headers, json=payload)
        response_json = response.json()

        if response_json.get("code") == "0":
            print(f">>> Success | Withdrawal of {amount:.8f} {token} to {address} successful.")
        else:
            print(f">>> Failed | Withdrawal of {amount:.8f} {token} to {address} failed. Error: {response.text}")

        sleep_duration = random.randint(10, 40)
        time.sleep(sleep_duration)


if __name__ == "__main__":
    withdraw_funds_to_cold_wallets(COLD_WALLET_ADDRESSES)
