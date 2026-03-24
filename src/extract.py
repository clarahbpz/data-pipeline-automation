import requests
import pandas as pd
from datetime import datetime

def fetch_currency_data():
    """Busca USD e EUR em relação ao Real (BRL)"""
    url = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # Transformando o JSON aninhado em uma lista plana
        processed = []
        for coin in data.values():
            processed.append({
                "moeda": coin["code"],
                "valor_brl": float(coin["bid"]),
                "data_consulta": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
        return pd.DataFrame(processed)
    else:
        raise Exception("Erro ao acessar AwesomeAPI")

def fetch_btc_data():
    """Busca preço do Bitcoin em BRL via CoinGecko"""
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=brl"
    response = requests.get(url)
    if response.status_code == 200:
        price = response.json()["bitcoin"]["brl"]
        return pd.DataFrame([{
            "moeda": "BTC",
            "valor_brl": float(price),
            "data_consulta": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }])
    return pd.DataFrame()