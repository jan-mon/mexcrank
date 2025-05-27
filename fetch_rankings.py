import ccxt
import csv
from datetime import datetime

# MEXC取引所を設定（API制限を考慮）
exchange = ccxt.mexc({'enableRateLimit': True})

# 全シンボルを取得
keys = exchange.load_markets().keys()

# symbols 初期化
symbols = []
for key in keys:
    if key.endswith('/USDT:USDT'):
        symbols.append(key.replace("/USDT:USDT", ""))

# 現在時刻（UTC）
timestamp = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

# CSVに追記
with open('rankings.csv', mode='a', newline='') as file:
    writer = csv.writer(file)
    for rank, symbol in enumerate(symbols, start=1):
        writer.writerow([timestamp, rank, symbol])

print(f"{timestamp}: {len(symbols)} symbols saved.")
