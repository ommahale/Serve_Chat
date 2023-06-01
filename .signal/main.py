from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def index():
    return {"message":"This is a signalling server microservice"}

if __name__=="__main__":
    uvicorn.run(host="0.0.0.0",port=8001,app="main:app")