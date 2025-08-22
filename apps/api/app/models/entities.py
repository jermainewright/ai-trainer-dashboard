from datetime import datetime

from sqlalchemy import JSON, Column, DateTime, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from app.core.database import Base


class Dataset(Base):
    __tablename__ = "datasets"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(120), nullable=False)
    path = Column(String(255), nullable=False)
    row_count = Column(Integer, default=0)
    target_column = Column(String(120), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)


class Experiment(Base):
    __tablename__ = "experiments"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(120), nullable=False)
    model_family = Column(String(80), nullable=False)
    algorithm = Column(String(80), nullable=False)
    status = Column(String(40), default="queued")
    params = Column(JSON, nullable=False)
    metrics = Column(JSON, default={})
    notes = Column(Text, default="")
    created_at = Column(DateTime, default=datetime.utcnow)

    runs = relationship("TrainingRun", back_populates="experiment", cascade="all,delete")


class TrainingRun(Base):
    __tablename__ = "training_runs"

    id = Column(Integer, primary_key=True, index=True)
    experiment_id = Column(Integer, ForeignKey("experiments.id"), nullable=False)
    epoch = Column(Integer, nullable=False)
    step = Column(Integer, nullable=False)
    loss = Column(Float, nullable=False)
    val_loss = Column(Float, nullable=False)
    metric_name = Column(String(80), default="accuracy")
    metric_value = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    experiment = relationship("Experiment", back_populates="runs")
