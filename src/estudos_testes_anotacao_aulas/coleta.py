# src/coleta.py: etapa E do pipeline
import json
from datetime import datetime, timezone
from pathlib import Path
import requests

URL = "https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL"
RAW_DIR = Path("data/raw")

def coletar_cotacoes() -> dict:
    """Busca as ultimas cotacoes de dolar e euro."""
    resposta = requests.get(URL, timeout=10)
    resposta.raise_for_status()
    return resposta.json()

cotacoes = coletar_cotacoes()
print (cotacoes)
