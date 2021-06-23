from fastapi import FastAPI

from pydantic import BaseModel

from money import ValorMoedas

app = FastAPI()


# Rota Raiz
@app.get("/")
def raiz():
    return{"Ola Mundo!"}


# Criar model
class Moedas(BaseModel):
    name: str
    high: str
    
# Cria a Base de dados
codemoney = ValorMoedas()

codemoney.consulta_USDBRL()
dolarCota = [
    Moedas(
        name=codemoney.nome, 
        high=codemoney.valor,
        )
]

codemoney.consulta_EURBRL()
euroCota = [
    Moedas(
        name=codemoney.nome, 
        high=codemoney.valor,
        )
]

codemoney.consulta_BTCBRL()
bitCota = [
    Moedas(
        name=codemoney.nome, 
        high=codemoney.valor,
        )
]

# Rota Get All
@app.get("/moedas")
def get_todos_as_moedas():
    return dolarCota, euroCota, bitCota


# Rota Get nameCode
@app.get("/moedas/converte_dollar/{DolLar}")
def get_moeda_usando_nome1(unidades: float):
    if unidades:

        for us in dolarCota:
            dolar=us.high 
        valor_em_dolar = unidades * float(dolar)
        
        for eu in euroCota:
            euro=eu.high 
        valor_euro = float(valor_em_dolar)/float(euro)
        
        for bit in bitCota:
            bitcoin=bit.high
        valor_bitcoin = float(valor_em_dolar)/float(bitcoin)

        return {
                "Moedas":
                    {
                        "unidades de dolar":unidades,
                        "Dolar/Real":valor_em_dolar, 
                        "Dolar/Euro":valor_euro,
                        "Dolar/BitCoin":valor_bitcoin
                    }
                }

