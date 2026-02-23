from fastapi import FastAPI

app = FastAPI()

@app.get("/echo")
async def echo(message: str):
    return {"message": message}
