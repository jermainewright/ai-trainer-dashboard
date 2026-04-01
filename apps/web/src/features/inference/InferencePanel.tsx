import { useMemo, useState } from "react";

const prompts = [
  "Classify: urgent support ticket",
  "Predict: churn risk for account #204",
  "Score sentiment: app review"
];

export function InferencePanel() {
  const [seed, setSeed] = useState(0);
  const result = useMemo(() => {
    const confidence = (0.74 + (seed % 20) * 0.01).toFixed(2);
    return `Prediction: Positive Signal | Confidence: ${confidence}`;
  }, [seed]);

  return (
    <div className="stack">
      <h3>Inference Lab</h3>
      <p>Run instant A/B style checks against model candidates.</p>
      <ul className="prompt-list">
        {prompts.map((prompt) => (
          <li key={prompt}>{prompt}</li>
        ))}
      </ul>
      <button onClick={() => setSeed((v) => v + 1)}>Run Comparative Inference</button>
      <output>{result}</output>
    </div>
  );
}
