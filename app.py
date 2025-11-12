from flask import Flask, jsonify, render_template  # render_template を追加
import requests
from datetime import datetime
import json
import os

app = Flask(__name__)

def get_crypto_prices():
    """暗号通貨の価格を取得"""
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "bitcoin,ethereum",
        "vs_currencies": "usd,jpy"
    }
    
    response = requests.get(url, params=params)
    return response.json()

def save_prices_to_file(price_data):
    """価格データをファイルに保存"""
    filename = "prices.json"

    if os.path.exists(filename):
        with open(filename, 'r') as f:
            history = json.load(f)
    else:
        history = []

    history.append(price_data)

    with open(filename, 'w') as f:
        json.dump(history, f, indent=2)


@app.route('/')
def index():
    """トップページ - HTMLを表示"""
    return render_template('index.html')

@app.route('/prices')
def prices():
    """価格を取得"""
    data = get_crypto_prices()
    
    # 現在時刻を取得
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # 見やすく整形
    result = {
        "updated_at": now,
        "data": {
            "bitcoin": {
                "usd": data['bitcoin']['usd'],
                "jpy": data['bitcoin']['jpy'],
                "name": "ビットコイン"
            },
            "ethereum": {
                "usd": data['ethereum']['usd'],
                "jpy": data['ethereum']['jpy'],
                "name": "イーサリアム"
            }
        }
    }
    
    # ファイルに保存
    save_prices_to_file(result)
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)