import os
from sqlalchemy import create_engine

def get_engine(db_path="database/warehouse.db"):
    # Extrai o nome da pasta (database)
    folder = os.path.dirname(db_path)
    
    # Se a pasta não existir e não for o diretório atual, cria ela
    if folder and not os.path.exists(folder):
        os.makedirs(folder)
        print(f"📁 Pasta '{folder}' criada com sucesso!")
        
    return create_engine(f"sqlite:///{db_path}")

def save_to_sql(df, table_name, engine):
    df.to_sql(table_name, con=engine, if_exists='append', index=False)
    print(f"✅ Dados salvos com sucesso na tabela {table_name}!")