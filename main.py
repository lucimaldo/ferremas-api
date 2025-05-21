from fastapi import FastAPI
from services.ferremas_api import get_products
from services.stripe_api import create_payment_intent
from services.currency_api import get_usd_to_clp

app = FastAPI(
    title="FERREMAS Integration API",
    description="Servicios de integración con API interna, Stripe y BCCh",
    version="1.0"
)

@app.get("/productos")
async def productos():
    return await get_products()

@app.get("/conversion")
async def conversion_dolar():
    valor = await get_usd_to_clp()
    return {"valor_dolar": valor}

@app.post("/pago")
def pagar(amount: int):
    intent = create_payment_intent(amount)
    return {"client_secret": intent.client_secret}