from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from app.core.database import SessionLocal
from app.models.entities import Experiment
from app.services.training_service import TrainingService

router = APIRouter()


@router.websocket("/ws/train/{experiment_id}")
async def train_ws(websocket: WebSocket, experiment_id: int):
    await websocket.accept()
    db = SessionLocal()
    try:
        experiment = db.query(Experiment).filter(Experiment.id == experiment_id).first()
        if experiment is None:
            await websocket.send_json({"error": "Experiment not found"})
            return

        for event in TrainingService(db).stream_training(experiment):
            await websocket.send_json(event)

        await websocket.send_json({"event": "complete", "experiment_id": experiment_id})
    except WebSocketDisconnect:
        pass
    finally:
        db.close()
