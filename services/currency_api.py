import httpx

async def get_usd_to_clp():
    url = "https://mindicador.cl/api/dolar"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()
        return data["serie"][0]["valor"]