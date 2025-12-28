import { useEffect, useRef } from "react";
import type { TrainingEvent } from "../types";

function simulatedEvent(epoch: number): TrainingEvent {
  const loss = Math.max(0.08, 1.2 / (epoch * 0.9));
  const valLoss = loss * (1 + Math.sin(epoch) * 0.08);
  const accuracy = Math.min(0.99, 0.52 + epoch * 0.032);
  return {
    experiment_id: 1,
    epoch,
    loss: Number(loss.toFixed(4)),
    val_loss: Number(valLoss.toFixed(4)),
    accuracy: Number(accuracy.toFixed(4))
  };
}

export function useTrainingSocket(
  experimentId: number | null,
  onEvent: (event: TrainingEvent) => void,
  onComplete: () => void
) {
  const timer = useRef<number | null>(null);

  useEffect(() => {
    if (!experimentId) return;
    let epoch = 0;
    let ws: WebSocket | null = null;

    const runSimulation = () => {
      timer.current = window.setInterval(() => {
        epoch += 1;
        onEvent(simulatedEvent(epoch));
        if (epoch >= 20) {
          if (timer.current) window.clearInterval(timer.current);
          onComplete();
        }
      }, 650);
    };

    try {
      ws = new WebSocket(`${window.location.protocol === "https:" ? "wss" : "ws"}://localhost:8000/ws/train/${experimentId}`);
      ws.onmessage = (message) => {
        const parsed = JSON.parse(message.data);
        if (parsed.event === "complete") onComplete();
        else if (!parsed.error) onEvent(parsed as TrainingEvent);
      };
      ws.onerror = () => {
        ws?.close();
        runSimulation();
      };
    } catch {
      runSimulation();
    }

    return () => {
      if (timer.current) window.clearInterval(timer.current);
      ws?.close();
    };
  }, [experimentId, onComplete, onEvent]);
}
