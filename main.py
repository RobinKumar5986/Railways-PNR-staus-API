from fastapi import FastAPI
from fastapi.responses import JSONResponse
import json
from pnrScraper import get_pnr_status

app = FastAPI()

@app.get("/status")
async def prn_status(pnr: str):
    prn_json = get_pnr_status(pnr)
    return prn_json