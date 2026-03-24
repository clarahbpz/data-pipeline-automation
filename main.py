from src.extract import fetch_currency_data, fetch_btc_data
from src.load import get_engine, save_to_sql
import pandas as pd

def run_pipeline():
    print("Iniciando Extração...")
    
    # 1. Extração
    df_currencies = fetch_currency_data()
    df_btc = fetch_btc_data()
    
    # 2. União (Transformação simples)
    df_final = pd.concat([df_currencies, df_btc], ignore_index=True)
    
    # 3. Carga
    engine = get_engine("database/warehouse.db")
    save_to_sql(df_final, "financial_history", engine)
    
    print("Pipeline finalizado com sucesso!")

if __name__ == "__main__":
    run_pipeline()