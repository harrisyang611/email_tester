from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/approve")
async def approve(token: str):
    # Log or store the approval decision
    print(f"Approved token: {token}")
    return HTMLResponse("<h2>✅ You have approved the request.</h2>")

@app.get("/reject")
async def reject(token: str):
    print(f"Rejected token: {token}")
    return HTMLResponse("<h2>❌ You have rejected the request.</h2>")