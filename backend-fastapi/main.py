import sys
sys.path.append("~/routers")

from fastapi import Depends, FastAPI
from typing import Optional

from routers import items, users

app = FastAPI()
app.include_router(items.router)
app.include_router(users.router)

@app.get("/")
async def root():
    return {"Hello": "World"}
