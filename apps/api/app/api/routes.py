from fastapi import APIRouter, Depends, File, UploadFile
from fastapi.responses import ORJSONResponse
from sqlalchemy.orm import Session

from app.models.entities import Experiment

from app.core.database import get_db
from app.schemas.contracts import ABTestRequest, ExperimentCreate, InferenceRequest
from app.services.dataset_service import DatasetService
from app.services.education_service import list_cards
from app.services.inference_service import InferenceService
from app.services.training_service import TrainingService

router = APIRouter(prefix="/v1", default_response_class=ORJSONResponse)


@router.get("/health")
def health() -> dict:
    return {"status": "ok"}


@router.post("/datasets")
async def upload_dataset(
    file: UploadFile = File(...),
    target_column: str | None = None,
    db: Session = Depends(get_db),
):
    payload = await file.read()
    dataset = DatasetService(db).save(file.filename, payload, target_column)
    return {"id": dataset.id, "name": dataset.name, "rows": dataset.row_count}


@router.get("/datasets")
def list_datasets(db: Session = Depends(get_db)):
    datasets = DatasetService(db).list()
    return [
        {
            "id": d.id,
            "name": d.name,
            "row_count": d.row_count,
            "target_column": d.target_column,
            "created_at": d.created_at,
        }
        for d in datasets
    ]


@router.post("/experiments")
def create_experiment(payload: ExperimentCreate, db: Session = Depends(get_db)):
    experiment = TrainingService(db).create_experiment(payload.model_dump())
    return {"id": experiment.id, "status": experiment.status}


@router.get("/experiments")
def list_experiments(db: Session = Depends(get_db)):
    experiments = db.query(Experiment).order_by(Experiment.created_at.desc()).all()
    return [
        {
            "id": exp.id,
            "name": exp.name,
            "model_family": exp.model_family,
            "algorithm": exp.algorithm,
            "status": exp.status,
            "params": exp.params,
            "metrics": exp.metrics,
            "created_at": exp.created_at,
        }
        for exp in experiments
    ]


@router.post("/inference")
def inference(payload: InferenceRequest):
    return InferenceService().run(payload.experiment_id, payload.payload)


@router.post("/ab-test")
def ab_test(payload: ABTestRequest):
    return InferenceService().ab_test(
        payload.control_experiment_id,
        payload.challenger_experiment_id,
        payload.samples,
    )


@router.get("/education/cards")
def education_cards():
    return list_cards()
