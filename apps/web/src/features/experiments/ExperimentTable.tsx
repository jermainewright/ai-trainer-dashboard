import type { Experiment } from "../../types";

export function ExperimentTable({ experiments }: { experiments: Experiment[] }) {
  return (
    <div>
      <h3>Experiment Arena</h3>
      <table>
        <thead>
          <tr>
            <th>Name</th>
            <th>Family</th>
            <th>Algorithm</th>
            <th>Status</th>
          </tr>
        </thead>
        <tbody>
          {experiments.map((exp) => (
            <tr key={exp.id}>
              <td>{exp.name}</td>
              <td>{exp.model_family}</td>
              <td>{exp.algorithm}</td>
              <td><span className={`status status-${exp.status}`}>{exp.status}</span></td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
