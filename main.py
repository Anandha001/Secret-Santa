from fastapi import FastAPI
from routes import router

app = FastAPI(
    title="Secret Santa",
    version="1.0",
    contact={
        "name": "Anandha",
        "email": "anandhakannan0001@gmail.com",
    },
)
app.include_router(router, prefix="/api/v1")
