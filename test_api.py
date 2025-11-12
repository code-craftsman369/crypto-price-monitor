import requests
import time

# CoinGecko APIのURL
url = "http://api.coingecko.com/api/v3/simple/price"

# テスト1：全部一緒に取得
print("=== テスト1：全通貨一緒に取得 ===")
crypto_ids = [
    "bitcoin", "ethereum", "ripple", "solana",
    "dogecoin", "tether", "sui", "mantle",
    "hyperliquid", "polkadot"
]

# パラメータ
params = {
    "ids": ",".join(crypto_ids),
    "vs_currencies": "usd,jpy"
}

# APIにリクエストを送る
response = requests.get(url, params=params)
data = response.json()

for crypto_id in crypto_ids:
    if crypto_id in data:
        print(f"✅ {crypto_id}")
    else:
        print(f"❌ {crypto_id}")

print(f"\n取得できた通貨数: {len(data)}/10")


# テスト2：ethereum だけ単独で取得
print("\n=== テスト2：ethereum 単独で取得 ===")
time.sleep(1)
params = {"ids": "ethereum", "vs_currencies": "usd,jpy"}
response = requests.get(url, params=params)
data = response.json()
print(data)

# テスト3：ripple だけ単独で取得
print("\n=== テスト3：ripple 単独で取得 ===")
time.sleep(1)
params = {"ids": "ripple", "vs_currencies": "usd,jpy"}
response = requests.get(url, params=params)
data = response.json()
print(data)




