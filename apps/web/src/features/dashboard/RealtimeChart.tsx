import { Area, AreaChart, CartesianGrid, ResponsiveContainer, Tooltip, XAxis, YAxis } from "recharts";
import type { TrainingEvent } from "../../types";

export function RealtimeChart({ events }: { events: TrainingEvent[] }) {
  return (
    <div style={{ width: "100%", height: 280 }}>
      <ResponsiveContainer>
        <AreaChart data={events}>
          <defs>
            <linearGradient id="lossColor" x1="0" y1="0" x2="0" y2="1">
              <stop offset="5%" stopColor="#ffde59" stopOpacity={0.8} />
              <stop offset="95%" stopColor="#ffde59" stopOpacity={0} />
            </linearGradient>
            <linearGradient id="accColor" x1="0" y1="0" x2="0" y2="1">
              <stop offset="5%" stopColor="#8be28b" stopOpacity={0.8} />
              <stop offset="95%" stopColor="#8be28b" stopOpacity={0} />
            </linearGradient>
          </defs>
          <CartesianGrid strokeDasharray="3 3" stroke="#6b4f2a" />
          <XAxis dataKey="epoch" stroke="#3e2a14" />
          <YAxis domain={[0, 1.5]} stroke="#3e2a14" />
          <Tooltip />
          <Area type="monotone" dataKey="loss" stroke="#ad6f00" fill="url(#lossColor)" />
          <Area type="monotone" dataKey="accuracy" stroke="#2e7d32" fill="url(#accColor)" />
        </AreaChart>
      </ResponsiveContainer>
    </div>
  );
}
