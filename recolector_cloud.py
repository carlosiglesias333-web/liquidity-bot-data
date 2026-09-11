import requests
from datetime import datetime, timezone

print("=" * 60)
print("PRUEBA LIQUIDITY BOT - GITHUB CLOUD")
print("=" * 60)

print("UTC:", datetime.now(timezone.utc))

exchanges = {
    "BINANCE": "https://fapi.binance.com/fapi/v1/ticker/price?symbol=BTCUSDT",
    "BYBIT": "https://api.bybit.com/v5/market/tickers?category=linear&symbol=BTCUSDT",
    "GATE": "https://api.gateio.ws/api/v4/futures/usdt/tickers?contract=BTC_USDT",
    "OKX": "https://www.okx.com/api/v5/market/ticker?instId=BTC-USDT-SWAP"
}

for nombre, url in exchanges.items():

    try:
        r = requests.get(url, timeout=10)

        print(
            nombre,
            "HTTP",
            r.status_code
        )

    except Exception as e:

        print(
            nombre,
            "ERROR:",
            e
        )

print("=" * 60)
print("PRUEBA TERMINADA")
print("=" * 60)
