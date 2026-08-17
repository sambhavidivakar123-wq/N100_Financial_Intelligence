from fastapi import APIRouter

router = APIRouter()

@router.get("/documents")
def get_documents():
    return {"message": "Documents endpoint working"}