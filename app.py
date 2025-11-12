from flask import Flask, jsonify, render_template  # render_template を追加
import requests
from datetime import datetime
import json
import os
import time

app = Flask(__name__)

def get_crypto_prices():
    """暗号通貨の価格を取得(リトライ機能付き)"""
    url = "https://api.coingecko.com/api/v3/simple/price"

    # 取得する暗号通貨のリスト
    crypto_ids = [
        "bitcoin",
        "ethereum",
        "ripple",
        "solana",
        "dogecoin",
        "tether",
        "sui",
        "mantle",
        "hyperliquid",
        "polkadot"
    ]

    params = {
        "ids": ",".join(crypto_ids),
        "vs_currencies": "usd,jpy"
    }
    
    max_retries = 3
    for attempt in range(max_retries):
        try:
            response = requests.get(url, params=params, timeout=10)

            # レート制限の場合
            if response.status_code == 429:
                print(f"レート制限: {attempt + 1}回目、5秒待機...")
                time.sleep(5)
                continue

            # 成功
            if response.status_code == 200:
                return response.json()
            
        except Exception as e:
            print(f"エラー: {e}")
            if attempt < max_retries - 1:
                time.sleep(2)    

    # 全て失敗した場合、空の辞書を返す
    return {}

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
    try:
        data = get_crypto_prices()
    
        # 現在時刻を取得
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # 通貨名の辞書
        crypto_names = {
            "bitcoin": "ビットコイン",
            "ethereum": "イーサリアム",
            "ripple": "リップル",
            "solana": "ソラナ",
            "dogecoin": "ドージコイン",
            "tether": "テザー",
            "sui": "スイ",
            "mantle": "マントル",
            "hyperliquid": "ハイパーリキッド",
            "polkadot": "ポルカドット"
        }

        # データを整形（ループで自動生成）
        result_data = {}
        for crypto_id in data:
            result_data[crypto_id] = {
                "usd": data[crypto_id].get('usd'),
                "jpy": data[crypto_id].get('jpy'),
                "name": crypto_names.get(crypto_id, crypto_id)
            }

        result = {
            "updated_at": now,
            "data": result_data
        }
    
        # ファイルに保存
        save_prices_to_file(result)

        return jsonify(result)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)