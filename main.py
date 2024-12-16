from fastapi import FastAPI, HTTPException
import requests
from models.stock import StockSubmission
from utils.auth import get_access_token
from services.lmePassport import submit_stock

app = FastAPI()

CLIENT_ID = "your_client_id"
CLIENT_SECRET = "your_client_secret"

@app.post("/submit-stock")
async def submit_stock_api(data: StockSubmission):
    try:
        token = get_access_token(CLIENT_ID, CLIENT_SECRET)
        result = submit_stock(data.dict(), token)
        return {"message": "Submission successful", "result": result}
    except requests.exceptions.HTTPError as e:
        raise HTTPException(status_code=400, detail=str(e))
