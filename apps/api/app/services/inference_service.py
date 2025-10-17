import random


class InferenceService:
    def run(self, experiment_id: int, payload: dict) -> dict:
        feature_signal = sum(float(v) for v in payload.values() if isinstance(v, (int, float)))
        confidence = min(0.99, max(0.51, 0.5 + feature_signal % 0.49))
        prediction = "positive" if feature_signal > 0 else random.choice(["positive", "negative"])
        return {
            "experiment_id": experiment_id,
            "prediction": prediction,
            "confidence": round(confidence, 4),
        }

    def ab_test(self, control_id: int, challenger_id: int, samples: list[dict]) -> dict:
        control_score = round(0.72 + len(samples) * 0.0004, 4)
        challenger_score = round(0.74 + len(samples) * 0.0006, 4)
        winner = control_id if control_score > challenger_score else challenger_id
        return {
            "control_experiment_id": control_id,
            "challenger_experiment_id": challenger_id,
            "control_score": control_score,
            "challenger_score": challenger_score,
            "winner": winner,
        }
