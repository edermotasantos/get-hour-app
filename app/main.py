import requests

from datetime import datetime, time

from fastapi import FastAPI

from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def get_hour():
    timezone = 'America/Sao_Paulo'
    url = 'http://worldtimeapi.org/api/timezone/' + timezone
    result = requests.get(url)
    hour = result.json()['datetime'][11:19]
    return hour
