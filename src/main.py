from typing import Union

from fastapi import FastAPI

from api.user.router import router as UserRoutes

app = FastAPI()

#handler = Mangum(app)

@app.get("/")
def read_root():
    return {"Hello": "World"}

app.include_router(UserRoutes,prefix="/guardian")


