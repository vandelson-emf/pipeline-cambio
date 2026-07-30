'''
Este script captura a cotação do câmbio do dólar (usd) para o real (brl), salva o dado original em formato .json com o timestamp da coleta:
    data/raw/cambio_usd_brl_AAAA-MM-DD_HH-MM-SS.json

'''

import json
import numpy as np
import time
import requests

from datetime import datetime
from pathlib import Path

# URL da API para obter a cotação do dólar
URL = "https://economia.awesomeapi.com.br/json/last/USD-BRL"

# Path para salvar as cotações em formato JSON
SAVE_PATH = Path("data/raw")

def get_cotacao_dolar():

    # Cria o diretório 'raw' se não existir
    SAVE_PATH.mkdir(parents=True, exist_ok=True) 

    # Faz a requisição GET para a API
    response = requests.get(URL, timeout=10)
    # Levanta uma exceção se a requisição falhar
    response.raise_for_status()

    # Verifica se a requisição foi bem-sucedida
    if response.status_code == 200:
        data = response.json()
        
        # Cria o timestamp para o nome do arquivo
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"{SAVE_PATH}/cambio_usd_brl_{timestamp}.json"
        
        # Salva os dados em formato JSON
        with open(filename, 'w', encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print(f"Cotação do dólar para real salva em: {filename}")
        return data
    else:
        print("Erro ao obter a cotação do dólar.")
        return None

if __name__ == "__main__":

    gets = 1
    for _ in range(gets):  # Coleta 1 vez
        print (f'Coleta {_+1} de {gets}')
        get_cotacao_dolar()

        if _ < gets - 1:  # Evita aguardar após a última coleta
            sleep = np.random.randint(10, 60)  # Gera um tempo aleatório entre 10 e 60 segundos
            print (f"Aguardando {sleep} segundos antes da próxima requisição...")
            time.sleep(sleep)  # Aguarda um tempo aleatório entre as requisições