import requests

# API de cotação de moedas: https://docs.awesomeapi.com.br/api-de-moedas

request = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL")
request = request.json()

cotacao_dolar = request['USDBRL']['bid']
cotacao_euro = request['EURBRL']['bid']

print(cotacao_dolar)
print(cotacao_euro)
