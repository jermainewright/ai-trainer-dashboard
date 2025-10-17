import random
import time
from collections.abc import Generator

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sqlalchemy.orm import Session

from app.models.entities import Experiment, TrainingRun


class TrainingService:
    def __init__(self, db: Session):
        self.db = db

    def create_experiment(self, payload: dict) -> Experiment:
        experiment = Experiment(**payload, status="running")
        self.db.add(experiment)
        self.db.commit()
        self.db.refresh(experiment)
        return experiment

    def stream_training(self, experiment: Experiment) -> Generator[dict, None, None]:
        base_loss = random.uniform(0.8, 1.4)
        for epoch in range(1, experiment.params.get("epochs", 10) + 1):
            loss = max(0.05, base_loss / (epoch * random.uniform(0.95, 1.1)))
            val_loss = loss * random.uniform(0.9, 1.2)
            metric = min(0.99, 0.45 + epoch * random.uniform(0.03, 0.055))

            run = TrainingRun(
                experiment_id=experiment.id,
                epoch=epoch,
                step=epoch,
                loss=loss,
                val_loss=val_loss,
                metric_name="accuracy",
                metric_value=metric,
            )
            self.db.add(run)
            self.db.commit()
            yield {
                "experiment_id": experiment.id,
                "epoch": epoch,
                "loss": round(loss, 4),
                "val_loss": round(val_loss, 4),
                "accuracy": round(metric, 4),
            }
            time.sleep(0.6)

        experiment.status = "completed"
        experiment.metrics = {"best_accuracy": round(metric, 4), "final_loss": round(loss, 4)}
        self.db.commit()

    def quick_classical_train(self, X, y, algorithm: str, params: dict) -> float:
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        if algorithm == "random_forest":
            model = RandomForestClassifier(n_estimators=params.get("n_estimators", 100), random_state=42)
        else:
            model = Pipeline([
                ("scale", StandardScaler()),
                ("mlp", MLPClassifier(hidden_layer_sizes=(64, 32), max_iter=300)),
            ])
        model.fit(X_train, y_train)
        return float(model.score(X_test, y_test))
