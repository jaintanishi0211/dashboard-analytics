from fastapi import APIRouter
from services.analytics import compute_stats

router = APIRouter()

@router.get("/stats")
def get_stats():
    return compute_stats()