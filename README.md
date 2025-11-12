# Crypto Price Monitor

CoinGecko APIを使った暗号通貨価格監視ツール

## 🌟 機能

- ✅ ビットコイン・イーサリアムの価格取得
- ✅ USD・JPY両方で表示
- ✅ タイムスタンプ付き
- ✅ 価格履歴をJSONファイルに保存
- ✅ きれいなWebページで表示
- ✅ 30秒ごとに自動更新

## 🛠 技術スタック

- **Python** 3.11
- **Flask** 3.1
- **CoinGecko API**
- **JSON** データストレージ

## 📦 インストール

### 1. リポジトリをクローン
```bash
git clone https://github.com/code-craftsman369/crypto-price-monitor.git
cd crypto-price-monitor
```

### 2. 依存パッケージをインストール
```bash
pip install flask requests
```

## 🚀 使い方

### サーバーを起動
```bash
python app.py
```

サーバーは `http://localhost:5002` で起動します。

## 📖 API エンドポイント

### 1. Webページ

**GET** `/`

ブラウザで見やすい価格表示ページ
```
http://localhost:5002/
```

---

### 2. 価格取得（JSON）

**GET** `/prices`
```bash
curl http://localhost:5002/prices
```

**レスポンス例**：
```json
{
  "updated_at": "2025-11-12 20:51:58",
  "data": {
    "bitcoin": {
      "usd": 104849,
      "jpy": 16237868,
      "name": "ビットコイン"
    },
    "ethereum": {
      "usd": 3544.76,
      "jpy": 548971,
      "name": "イーサリアム"
    }
  }
}
```

## 📊 データ構造

### 価格データオブジェクト
```json
{
  "updated_at": "2025-11-12 20:51:58",
  "data": {
    "bitcoin": {
      "usd": 104849,
      "jpy": 16237868,
      "name": "ビットコイン"
    },
    "ethereum": {
      "usd": 3544.76,
      "jpy": 548971,
      "name": "イーサリアム"
    }
  }
}
```

## 💾 データ保存

価格データは `prices.json` ファイルに履歴として保存されます。

**保存場所**：
```
crypto-price-monitor/
└── prices.json
```

**ファイル構造**：
```json
[
  {
    "updated_at": "2025-11-12 20:47:56",
    "data": {...}
  },
  {
    "updated_at": "2025-11-12 20:48:03",
    "data": {...}
  }
]
```

## 🎨 Webページ機能

- 💰 ビットコイン・イーサリアムの価格表示
- 🔄 更新ボタン
- ⏰ 30秒ごとに自動更新
- 📱 レスポンシブデザイン

## 📝 学習内容

このプロジェクトを通じて学んだこと：

- 外部API（CoinGecko）との連携
- `requests` ライブラリの使い方
- JSONデータの読み書き
- Flask による Web API 設計
- HTMLとJavaScriptの連携
- データの履歴保存
- エラーハンドリング

## 🔜 今後の改善予定

- [ ] より多くの暗号通貨に対応
- [ ] グラフ表示（価格の推移）
- [ ] アラート機能（価格変動通知）
- [ ] データベース連携（SQLite）
- [ ] 定期実行（APScheduler）

## 📄 ライセンス

MIT License

## 👤 作成者

Tatsu - Python Developer
- GitHub: [@code-craftsman369](https://github.com/code-craftsman369)

## 🙏 謝辞

- [CoinGecko API](https://www.coingecko.com/en/api) - 暗号通貨価格データ提供