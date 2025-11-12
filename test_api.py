import requests

# CoinGecko APIのURL
url = "http://api.coingecko.com/api/v3/simple/price"

# パラメータ（条件）
params = {
    "ids": "bitcoin,ethereum,ripple",
    "vs_currencies": "usd,jpy"
}

# APIにリクエストを送る
response = requests.get(url, params=params)
data = response.json()

# 結果を見やすく表示
print("=== 暗号通貨価格 ===")
print()

# ビットコインの価格
bitcoin_usd = data['bitcoin']['usd']
bitcoin_jpy = data['bitcoin']['jpy']
print(f"ビットコイン： ${bitcoin_usd:,} (¥{bitcoin_jpy:,})")

# イーサリアムの価格
ethereum_usd = data['ethereum']['usd']
ethereum_jpy = data['ethereum']['jpy']
print(f"イーサリアム: ${ethereum_usd:,} (¥{ethereum_jpy:,})")

# リップルの価格
ripple_usd = data['ripple']['usd']
ripple_jpy = data['ripple']['jpy']
print(f"リップル: ${ripple_usd:,} (¥{ripple_jpy:,})")

