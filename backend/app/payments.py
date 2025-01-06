from fastapi import FastAPI, Request
import datetime
from saltblock import base64_process
app = FastAPI()
@app.post("/payment")
def handle_payment(request: Request):
    wallet_id = request.form("capture")[0]

	batch_payment
	set credit_update to add response on success full detailed status. responses total