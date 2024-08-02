import azure.functions as func
from fastapi import FastAPI

from app.routers import user

app = FastAPI()
app.include_router(user.router, prefix="/users", tags=["Users"])


@app.get("/")
async def health():
    return {"message": "API health at 100%."}


async def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    return await func.AsgiMiddleware(app).handle_async(req, context)
