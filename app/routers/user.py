import logging
from typing import Dict

from fastapi import APIRouter, Path
from starlette.responses import JSONResponse

router = APIRouter()

fake_db: Dict[int, dict] = {}


@router.get("/")
async def get_users():
    logging.info("Retrieving users...")
    return list(fake_db.values())


@router.get("/{userId}")
async def get_user(
    user_id: int = Path(description="User ID", alias="userId"),
):
    logging.info(f"Retrieving user: {user_id}")
    try:
        return fake_db[user_id]
    except KeyError:
        return JSONResponse(status_code=404, content={"message": "User not found."})


@router.post("/")
async def create_user(user: dict):
    logging.info(f"Creating user: user")
    try:
        fake_db[user["userId"]] = user
        return {"message": "OK"}
    except KeyError:
        return JSONResponse(status_code=400, content={"message": "Missing key: 'userId'"})


@router.put("/{userId}")
async def update_user(
    user: dict,
    user_id: int = Path(description="User ID", alias="userId"),
):
    logging.info(f"Updating user: {user}")
    try:
        user.pop("userId", None)
        fake_db[user_id].update(user)
        return {"message": "OK"}
    except KeyError:
        return JSONResponse(status_code=404, content={"message": "User not found."})


@router.delete("/{userId}")
async def delete_user(
    user_id: int = Path(description="User ID", alias="userId"),
):
    logging.info(f"Deleting user: {user_id}")
    try:
        fake_db.pop(user_id)
        return {"message": "OK"}
    except KeyError:
        return JSONResponse(status_code=404, content={"message": "User not found."})
