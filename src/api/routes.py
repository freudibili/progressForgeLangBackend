from fastapi import APIRouter, HTTPException
from src.database import Database
from src.models.schemas import Vocabulary, Level

router = APIRouter()
db = Database()

@router.get("/vocabulary", response_model=list[Vocabulary])
async def get_vocabulary(limit: int = 10):
    result = db.execute_query(
        "SELECT * FROM vocabulary_entries LIMIT %s",
        params=(limit,)
    )
    return [Vocabulary(**row) for row in result]

@router.get("/vocabulary/{level_id}", response_model=list[Vocabulary])
async def get_vocabulary_by_level(level_id: str):
    result = db.execute_query(
        "SELECT * FROM vocabulary_entries WHERE level_id = %s",
        params=(level_id,)
    )
    if not result:
        raise HTTPException(status_code=404, detail="No vocabulary found for this level")
    return [Vocabulary(**row) for row in result]

@router.get("/levels", response_model=list[Level])
async def get_levels():
    result = db.execute_query("SELECT * FROM levels")
    return [Level(**row) for row in result] 