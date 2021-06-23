FROM Ubuntu:18.04
COPY . /app
RUN pip install fastapi && pip install pydantic
WORKDIR /app
CMD uvicorn converte_money_api:app --reload