import { FormEvent, useState } from "react";

interface Props {
  onExperimentCreated: (id: number) => void;
}

export function TrainingForm({ onExperimentCreated }: Props) {
  const [name, setName] = useState("Golden Falcon v1");
  const [modelFamily, setModelFamily] = useState("llm");
  const [algorithm, setAlgorithm] = useState("qlora");
  const [learningRate, setLearningRate] = useState("0.0008");

  const submit = (event: FormEvent) => {
    event.preventDefault();
    onExperimentCreated(Date.now());
  };

  return (
    <form className="stack" onSubmit={submit}>
      <h3>Experiment Studio</h3>
      <label>
        Experiment Name
        <input value={name} onChange={(e) => setName(e.target.value)} />
      </label>
      <div className="two-column">
        <label title="Train classical models or modern LLM stacks.">
          Model Family
          <select value={modelFamily} onChange={(e) => setModelFamily(e.target.value)}>
            <option value="classical">Classical ML</option>
            <option value="llm">LLM Fine-Tuning</option>
          </select>
        </label>
        <label>
          Algorithm
          <select value={algorithm} onChange={(e) => setAlgorithm(e.target.value)}>
            <option value="random_forest">Random Forest</option>
            <option value="mlp">MLP Classifier</option>
            <option value="qlora">QLoRA</option>
          </select>
        </label>
      </div>
      <label>
        Learning Rate
        <input value={learningRate} onChange={(e) => setLearningRate(e.target.value)} />
      </label>
      <button type="submit">Launch Live Training</button>
    </form>
  );
}
