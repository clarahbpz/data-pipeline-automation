import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px
from datetime import datetime

# Configuração da Página
st.set_page_config(page_title="Financial Data Pipeline", layout="wide", page_icon="📊")

# Custom CSS para deixar mais elegante
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    </style>
    """, unsafe_allow_html=True)

def load_data():
    conn = sqlite3.connect('database/warehouse.db')
    df = pd.read_sql_query("SELECT * FROM financial_history ORDER BY data_consulta ASC", conn)
    conn.close()
    # Converte para datetime para garantir ordenação no gráfico
    df['data_consulta'] = pd.to_datetime(df['data_consulta'])
    return df

# Header
st.title("📊 Financial Data Warehouse Dashboard")
st.markdown(f"**Status do Pipeline:** ✅ Ativo | **Última Atualização:** {datetime.now().strftime('%d/%m/%Y %H:%M')}")
st.write("---")

try:
    df = load_data()
    moedas = df['moeda'].unique()

    # --- SEÇÃO 1: MÉTRICAS (KPIs) ---
    st.subheader("💰 Cotações Atuais (BRL)")
    cols = st.columns(len(moedas))
    
    for i, moeda in enumerate(moedas):
        dados_moeda = df[df['moeda'] == moeda]
        valor_atual = dados_moeda['valor_brl'].iloc[-1]
        
        # Cálculo de variação simples se houver mais de um registro
        if len(dados_moeda) > 1:
            valor_anterior = dados_moeda['valor_brl'].iloc[-2]
            delta = f"{((valor_atual / valor_anterior) - 1) * 100:.2f}%"
        else:
            delta = None
            
        cols[i].metric(label=f"Paridade {moeda}/BRL", value=f"R$ {valor_atual:,.2f}", delta=delta)

    st.write("---")

    # --- SEÇÃO 2: GRÁFICOS INDIVIDUAIS ---
    st.subheader("📈 Análise de Tendência Histórica")
    
    # Criando abas para não poluir a tela, ou colunas. Vamos de colunas para ver tudo junto.
    for moeda in moedas:
        dados_plot = df[df['moeda'] == moeda]
        
        # Define cores diferentes para cada moeda
        cor = {"USD": "#1f77b4", "EUR": "#ff7f0e", "BTC": "#2ca02c"}.get(moeda, "#7f7f7f")
        
        fig = px.line(
            dados_plot, 
            x='data_consulta', 
            y='valor_brl',
            title=f"Evolução Temporal: {moeda}",
            labels={'valor_brl': 'Preço (R$)', 'data_consulta': 'Data da Coleta'},
            markers=True
        )
        
        fig.update_traces(line_color=cor)
        fig.update_layout(
            hovermode="x unified",
            margin=dict(l=20, r=20, t=50, b=20),
            height=350
        )
        
        st.plotly_chart(fig, use_container_width=True)

    # --- SEÇÃO 3: TABELA TÉCNICA ---
    with st.expander("🔍 Visualizar Dados Brutos do SQL"):
        st.write("Estes dados são extraídos diretamente do arquivo `warehouse.db` via SQLAlchemy.")
        st.dataframe(df.sort_values(by='data_consulta', ascending=False), use_container_width=True)

except Exception as e:
    st.error(f"Erro ao carregar dados: {e}")
    st.info("Dica: Certifique-se de que o arquivo 'database/warehouse.db' existe e contém dados.")