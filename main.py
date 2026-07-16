from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(title="EduTrack API", version="1.0.0")

class TaskWeight(BaseModel):
    task_name: str
    weight: int
    status: str

@app.get("/")
def read_root():
    return {"message": "EduTrack API is running. Go to /docs for Swagger UI."}

@app.get("/analytics/burn-down", response_model=List[dict])
def get_burn_down_data():
    # Заглушка для графика на фронтенде
    return [
        {"day": "Day 1", "remaining_weight": 50},
        {"day": "Day 2", "remaining_weight": 40},
        {"day": "Day 3", "remaining_weight": 35},
        {"day": "Day 4", "remaining_weight": 20},
        {"day": "Day 5", "remaining_weight": 0},
    ]