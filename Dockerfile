FROM python:3
COPY . /app
RUN pip install requirements.txt
WORKDIR /app
CMD python converte_money_api.py