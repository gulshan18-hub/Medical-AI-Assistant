from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/")
def list_users():
    return {"users": []}


@router.get("/{user_id}")
def get_user(user_id: int):
    return {"id": user_id, "status": "placeholder"}
