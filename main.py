from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API en Render funcionando 🚀"}

@app.get("/query")
def get_data():
    return {"data": ["dato1", "dato2", "dato3"]}
