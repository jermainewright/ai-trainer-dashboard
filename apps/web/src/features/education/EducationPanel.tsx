const cards = [
  {
    topic: "Overfitting Watch",
    summary: "If training loss falls while validation loss rises, generalization is slipping.",
    tip: "Apply dropout, data augmentation, or early stopping."
  },
  {
    topic: "Learning Rate Scheduling",
    summary: "Warmup + decay gives smoother optimization for transformer workloads.",
    tip: "Try cosine decay with 5% warmup for stable convergence."
  },
  {
    topic: "Quantization",
    summary: "Lower precision weights can dramatically speed up inference.",
    tip: "Begin with post-training INT8 and benchmark latency/quality tradeoff."
  }
];

export function EducationPanel() {
  return (
    <div className="stack">
      <h3>Guided Concepts</h3>
      {cards.map((card) => (
        <article key={card.topic} className="tip-card">
          <strong>{card.topic}</strong>
          <p>{card.summary}</p>
          <small>{card.tip}</small>
        </article>
      ))}
    </div>
  );
}
