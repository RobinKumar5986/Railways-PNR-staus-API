import requests
from bs4 import BeautifulSoup
import re
import json

from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()
@app.get("/status")
async def prn_status(pnr: str):
    return {"hello":"world"}}
