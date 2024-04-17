from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

app.mount("/photos", StaticFiles(directory="photos"), name="photos")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Load the JSON data from a file
with open('wheels.json') as f:
    data = json.load(f)

@app.get("/")
def read_root():
    return data

@app.get("/wheels")
def read_wheels():
    return data['wheels']

@app.get("/wheels/{wheel_name}")
def read_item(wheel_name: str):
    for wheel in data['wheels']:
        if wheel['name'] == wheel_name:
            return wheel
    return {"error": "Wheel not found"}

@app.get("/tires")
def read_tires():
    return data['tires']

@app.get("/tires/{tire_name}")
def read_item(tire_name: str):
    for tire in data['tires']:
        if tire['name'] == tire_name:
            return tire
    return {"error": "Tire not found"} 
