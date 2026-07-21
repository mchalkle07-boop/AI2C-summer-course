# Example from docs (simplified):
from fastapi import FastAPI

app = FastAPI()

@app.get("/root")
async def root():
    return {"message": "Hello World"}