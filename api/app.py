from fastapi import FastAPI

app = FastAPI()


@app.get("/gpt")
def read_root():
    return {"Hello": "World"}