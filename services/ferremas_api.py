import httpx
import os
from dotenv import load_dotenv

load_dotenv()
BASE_URL = "https://ea2p2assets-production.up.railway.app"
TOKEN = os.getenv("FERREMAS_TOKEN")

async def get_products():
    headers = {"Authorization": f"Bearer {TOKEN}"}
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}/productos", headers=headers)
        return response.json()