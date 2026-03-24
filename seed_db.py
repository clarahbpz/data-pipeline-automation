import sqlite3
import pandas as pd
from datetime import datetime, timedelta
import random

def generate_seed_data():
    conn = sqlite3.connect('database/warehouse.db')
    moedas = ['USD', 'EUR', 'BTC']
    bases = {'USD': 5.80, 'EUR': 6.10, 'BTC': 540000.00}
    
    dados = []
    hoje = datetime.now()

    for i in range(7, 0, -1):  # Últimos 7 dias
        data_fake = (hoje - timedelta(days=i)).strftime("%Y-%m-%d %H:%M:%S")
        for moeda in moedas:
            # Simula uma variação aleatória de 1%
            valor = bases[moeda] * (1 + random.uniform(-0.01, 0.01))
            dados.append({
                "moeda": moeda,
                "valor_brl": round(valor, 2),
                "data_consulta": data_fake
            })
    
    df_seed = pd.DataFrame(dados)
    df_seed.to_sql("financial_history", conn, if_exists='append', index=False)
    conn.close()
    print("✅ Histórico de 7 dias gerado com sucesso para o BI!")

if __name__ == "__main__":
    generate_seed_data()