from fastapi import FastAPI
from pydantic_settings import BaseSettings

class Config(BaseSettings):
    name: str = "world"

config = Config()

app = FastAPI()

@app.get("/hello")
def hello() -> str:
    return f"Hello {config.name}!"
