# Automated Financial Data Pipeline (ETL & BI)
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://data-pipeline-automation-z4qnua8g4an8gcizhfrshq.streamlit.app/)

---

This project is a complete End-to-End Data Engineering Pipeline designed to ingest, process, and visualize financial indicators (Fiat Currencies and Crypto) in real-time. It simulates a professional production environment focusing on data resilience and automation.

## Project Objective

To demonstrate technical proficiency in ETL pipeline automation, SQL data modeling, and delivering business value through data visualization (BI).

## Architecture & Data Flow

The system follows a modular architecture divided into four main layers:

Ingestion (Extract): Python scripts consuming REST APIs from AwesomeAPI (USD/EUR) and CoinGecko (Bitcoin).

Processing (Transform): Data cleaning and normalization using Pandas, including type conversion and timestamp standardization.

Storage (Load): Persistence in a SQLite relational database using SQLAlchemy, employing an Append strategy to build historical series (Data Warehouse).

Orchestration (CI/CD): GitHub Actions serves as the orchestrator, running the pipeline daily via Cron Jobs to ensure the warehouse is updated serverless.

Visualization (BI): An interactive dashboard built with Streamlit and Plotly for trend analysis and KPI monitoring.

## Tech Stack

Language: Python 3.10+

Data Manipulation: Pandas

Database & ORM: SQLite, SQLAlchemy

Visualization: Streamlit, Plotly

DevOps/Automation: GitHub Actions (YAML)

## Project Structure

data-pipeline-automation/
├── .github/workflows/

│   └── daily_etl.yml

├── src/

│   ├── extract.py 

│   ├── transform.py 

│   └── load.py

├── database/

│   └── warehouse.db  
├── app.py            
├── main.py           
├── requirements.txt  
└── README.md

## How to Run

#### Prerequisites
Ensure you have Python installed. Clone the repository and install the dependencies:

pip install -r requirements.txt

#### Run the Pipeline
To manually trigger the extraction and save data to the SQL database:

python main.py

#### Launch the Dashboard
To visualize the data in your browser:

streamlit run app.py

#### Developed by Clara Hilbert Polizel 
Computer Engineering Student at Universidade Federal de Goiás (UFG)
