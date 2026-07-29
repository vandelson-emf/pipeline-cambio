# teste_ambiente.py — valida o ambiente do modulo M3
import requests
import pandas
import sqlalchemy
import pymongo

print("requests   :", requests.__version__)
print("pandas     :", pandas.__version__)
print("SQLAlchemy :", sqlalchemy.__version__)
print("pymongo    :", pymongo.version)
print()
print("Ambiente ok! Voce esta pronto para a Aula 1.")