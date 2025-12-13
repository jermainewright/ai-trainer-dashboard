export interface Experiment {
  id: number;
  name: string;
  model_family: "classical" | "llm";
  algorithm: string;
  status: string;
  params: Record<string, unknown>;
  metrics: Record<string, unknown>;
}

export interface TrainingEvent {
  experiment_id: number;
  epoch: number;
  loss: number;
  val_loss: number;
  accuracy: number;
}
