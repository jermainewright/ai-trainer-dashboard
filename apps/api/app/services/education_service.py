EDUCATION_CARDS = [
    {
        "topic": "Overfitting",
        "summary": "Overfitting happens when model performance on training data improves while validation performance stagnates.",
        "tip": "Enable early stopping and add regularization to improve generalization.",
    },
    {
        "topic": "Learning Rate Scheduling",
        "summary": "Schedulers gradually adjust learning rate for stable convergence.",
        "tip": "Start with cosine decay for transformer-like workloads.",
    },
    {
        "topic": "Quantization",
        "summary": "Quantization reduces model precision to lower memory and inference latency.",
        "tip": "Use post-training quantization for quick deployment wins.",
    },
]


def list_cards() -> list[dict]:
    return EDUCATION_CARDS
