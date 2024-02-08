import requests
from bs4 import BeautifulSoup
import re
import json

from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()
@app.get("/status")
async def prn_status(pnr: str):
    # Specify the URL of the website
    url = f"https://www.confirmtkt.com/pnr-status/{pnr}"

    # Send an HTTP request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')
        return response.text
    return response.text
