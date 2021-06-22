import requests

class ValorMoedas():
    """Classe que retorna os valores das moedas
    por meio de uma api publica
    """

    def __init__(self):
        self.valor = -1
        self.nome = ""
    
    def consulta_USDBRL(self):
        url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"
        retorno = requests.get(url)
        if (retorno.status_code==200):
            jsonparsed = retorno.json()

            self.nome = jsonparsed['USDBRL']['code']
            self.valor = jsonparsed['USDBRL']['high']
        else:
            self.valor = -1
            self.nome = ""
    
    def consulta_EURBRL(self):
        url = "https://economia.awesomeapi.com.br/json/last/EUR-BRL"
        retorno = requests.get(url)
        if (retorno.status_code==200):
            jsonparsed = retorno.json()

            self.nome = jsonparsed['EURBRL']['code']
            self.valor = jsonparsed['EURBRL']['high']
        else:
            self.valor = -1
            self.nome = ""
    
    def consulta_BTCBRL(self):
        url = "https://economia.awesomeapi.com.br/json/last/BTC-BRL"
        retorno = requests.get(url)
        if (retorno.status_code==200):
            jsonparsed = retorno.json()

            self.nome = jsonparsed['BTCBRL']['code']
            self.valor = jsonparsed['BTCBRL']['high']
        else:
            self.valor = -1
            self.nome = ""
