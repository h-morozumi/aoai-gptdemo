from fastapi import APIRouter, Depends, HTTPException


router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)

fake_items_db = {"plumbus": {"name": "Plumbus"}, "gun": {"name": "Portal Gun"}}

@router.get("/")
async def read_items():
    return fake_items_db

@router.get("/{user_id}")
async def read_item(user_id: str):
    if user_id not in fake_items_db:
        raise HTTPException(status_code=404, detail="User not found")
    return {"name": fake_items_db[user_id]["name"], "user_id": user_id}

@router.put(
    "/{user_id}",
    tags=["custom"],
    responses={403: {"description": "Operation forbidden"}},
)
async def update_item(user_id: str):
    if user_id != "plumbus":
        raise HTTPException(
            status_code=403, detail="You can only update the user: plumbus"
        )
    return {"user_id": user_id, "name": "The great Plumbus"}