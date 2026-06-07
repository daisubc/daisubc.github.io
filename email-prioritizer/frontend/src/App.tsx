import { useState } from "react";
import { fetchDemo, processGmail } from "./api";
import { googleConfigured, requestGmailToken } from "./google";
import { EmailCard } from "./components/EmailCard";
import type { ProcessResponse } from "./types";

export default function App() {
  const [data, setData] = useState<ProcessResponse | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  async function run(fn: () => Promise<ProcessResponse>) {
    setLoading(true);
    setError(null);
    try {
      setData(await fn());
    } catch (e) {
      setError(e instanceof Error ? e.message : String(e));
    } finally {
      setLoading(false);
    }
  }

  const onDemo = () => run(fetchDemo);
  const onGmail = () =>
    run(async () => {
      const token = await requestGmailToken();
      return processGmail(token, 15);
    });

  const counts = data
    ? data.emails.reduce(
        (acc, e) => ((acc[e.priority] = (acc[e.priority] ?? 0) + 1), acc),
        {} as Record<string, number>,
      )
    : null;

  return (
    <div className="app">
      <header className="header">
        <h1>📥 Inbox Triage</h1>
        <p className="tagline">
          Summarizes your emails and ranks them by priority using an open-source LLM.
        </p>
      </header>

      <div className="controls">
        <button onClick={onGmail} disabled={loading || !googleConfigured()} className="btn primary">
          {googleConfigured() ? "Connect Gmail" : "Gmail not configured"}
        </button>
        <button onClick={onDemo} disabled={loading} className="btn">
          Try the demo inbox
        </button>
      </div>

      {!googleConfigured() && (
        <p className="hint">
          Set <code>VITE_GOOGLE_CLIENT_ID</code> to enable live Gmail. The demo works without it.
        </p>
      )}

      {loading && <p className="status">Summarizing and prioritizing…</p>}
      {error && <p className="status error">⚠️ {error}</p>}

      {data && (
        <>
          <div className="summary-bar">
            <span>{data.emails.length} emails</span>
            {counts && (
              <>
                <span className="dot high">{counts.high ?? 0} high</span>
                <span className="dot medium">{counts.medium ?? 0} medium</span>
                <span className="dot low">{counts.low ?? 0} low</span>
              </>
            )}
            <span className="engine">
              {data.llm_used ? `🤖 ${data.model}` : "📐 heuristic mode"}
            </span>
          </div>
          <div className="list">
            {data.emails.map((e) => (
              <EmailCard key={e.id} email={e} />
            ))}
          </div>
        </>
      )}

      <footer className="footer">
        Read-only Gmail access · processed per-request · nothing stored.
      </footer>
    </div>
  );
}
