import type { ProcessedEmail } from "../types";

const COLORS: Record<string, string> = {
  high: "#e5484d",
  medium: "#f5a623",
  low: "#6b7280",
};

export function EmailCard({ email }: { email: ProcessedEmail }) {
  const color = COLORS[email.priority];
  return (
    <article className="card" style={{ borderLeftColor: color }}>
      <div className="card-top">
        <span className="badge" style={{ background: color }}>
          {email.priority} · {email.priority_score}
        </span>
        <span className="category">{email.category}</span>
        {email.action_required && <span className="action">Action needed</span>}
      </div>
      <h3 className="subject">{email.subject || "(no subject)"}</h3>
      <p className="sender">{email.sender}</p>
      <p className="summary">{email.summary}</p>
      {email.reason && <p className="reason">Why: {email.reason}</p>}
    </article>
  );
}
