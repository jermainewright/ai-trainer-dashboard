from pathlib import Path

import pandas as pd
from sqlalchemy.orm import Session

from app.core.config import settings
from app.models.entities import Dataset


class DatasetService:
    def __init__(self, db: Session):
        self.db = db
        Path(settings.upload_dir).mkdir(parents=True, exist_ok=True)

    def save(self, filename: str, content: bytes, target_column: str | None = None) -> Dataset:
        path = Path(settings.upload_dir) / filename
        path.write_bytes(content)
        frame = pd.read_csv(path)
        dataset = Dataset(
            name=filename,
            path=str(path),
            row_count=len(frame),
            target_column=target_column,
        )
        self.db.add(dataset)
        self.db.commit()
        self.db.refresh(dataset)
        return dataset

    def list(self) -> list[Dataset]:
        return self.db.query(Dataset).order_by(Dataset.created_at.desc()).all()
