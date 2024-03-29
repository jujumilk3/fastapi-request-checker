from fastapi import FastAPI, Request
from pprint import pprint

app = FastAPI()


@app.get("/")
def check(request: Request):
    pprint(request.__dict__)
    return {"status": "ok"}
