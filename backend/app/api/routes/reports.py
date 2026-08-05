from fastapi import APIRouter

router = APIRouter(prefix="/reports", tags=["reports"])


@router.post("/analyze")
def analyze_report():
    return {"message": "PDF and medical report summarization placeholder"}
