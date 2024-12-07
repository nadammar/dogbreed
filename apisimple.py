from fastapi import FastAPI 
 
 

# Initialiser l'application FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "API is working!"}

@app.get("/hello")
def read_root():
    return {"hello msg !"}
# Charger le modèle et définir les class