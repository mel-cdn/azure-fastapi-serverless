import logging

from fastapi import APIRouter

router = APIRouter()


@router.get("/{user_id}")
async def get_user(user_id: int):
    logging.info("Retrieving user \'%s\'...", user_id)
    return {
        "user_id": user_id,
        "username": 'vic',
        "firstname": 'Victor',
        "lastname": 'Magtanggol',
    }


@router.put("/{user_id}")
async def update_user(user_id: int):
    logging.info("Updating user \'%s\'...", user_id)
    return {
        "user_id": user_id,
        "username": 'vic',
        "firstname": 'Victor',
        "lastname": 'Magtanggol',
    }


@router.delete("/{user_id}")
async def delete_user(user_id: int):
    logging.info("Deleting user \'%s\'...", user_id)
    return {"message": "OK"}
