import requests

from fastapi import FastAPI

from pydantic import BaseModel

app = FastAPI()


@app.get("/timezones")
def timezones_disponiveis():
    url = 'http://worldtimeapi.org/api/timezone/'
    resposta = requests.get(url)
    timezones = resposta.json()
    return timezones
