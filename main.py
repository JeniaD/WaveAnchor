from fastapi import FastAPI
from data import packages

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello world"}

@app.get("/packages")
async def GetPackages():
    res = {}
    for package in packages:
        res[package.name] = package.toDict()
    return res
