from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field


class DatasetOut(BaseModel):
    id: int
    name: str
    row_count: int
    target_column: str | None
    created_at: datetime


class ExperimentCreate(BaseModel):
    name: str
    model_family: str = Field(pattern="^(classical|llm)$")
    algorithm: str
    params: dict[str, Any]
    notes: str = ""


class ExperimentOut(BaseModel):
    id: int
    name: str
    model_family: str
    algorithm: str
    status: str
    params: dict[str, Any]
    metrics: dict[str, Any]
    notes: str
    created_at: datetime


class InferenceRequest(BaseModel):
    experiment_id: int
    payload: dict[str, Any]


class InferenceResponse(BaseModel):
    experiment_id: int
    prediction: str
    confidence: float


class ABTestRequest(BaseModel):
    control_experiment_id: int
    challenger_experiment_id: int
    samples: list[dict[str, Any]]
