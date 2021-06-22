# API de conversão monetária

A aplicação faz uso de uma api pública para converter unidade em dolar para as principais (porem nem todas) moedas em circulação.

A aplicação visa mostrar de forma suscinta valores atualizados do Dolar, Euro e BitCoin convertidos em Real 
Brasileiro atravez da API Pública AwesomeAPI "API de Cotações de Moedas".

A aplicação converte e mostra os valores no formato Json nativamente sem a necessidade de conversão explicita no código.

# Baixando o projeto

Para executar o projeto em seu ambiente faça um clone do repositorio github no seguinte endereço:

https://github.com/Aleleonel/conversor_monetario.git

os seguintes arquivos devem permanecer na mesma pasta
    1 - converte_money_api.py
    2 - money.py

Atenção: O projeto foi desenvolvido em container docker ubuntu com python3

framework utilizado: VSCode


Para rodar o projeto via docker execute o Build do arquivo Dockerfile

# Para rodar e testar o projeto

    execute no terminal na pasta do projeto:   
        uvicorn converte_money_api:app --reload

    depois com control apertado clique no endereço a baixo:
        http://127.0.0.1:8000
    
# Para Testar o Projeto
    digite http://127.0.0.1:8000/docs

    execute o metodo GET/ raiz para ver um Olá mundo

    execute o metodo GET / Todas as moedas para ver todas as moedas 

    execute o metodo GET / converte_dollar para per as conversões do dolar nas principais moedas 

# O que esta faltando

Não traz todas as moedas como por exemplo ETH
Não foi implementado nenhuma tratativa de erro


