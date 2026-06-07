import type { ProcessResponse } from "./types";

const API_BASE = import.meta.env.VITE_API_BASE ?? "http://localhost:8000";

async function handle(res: Response): Promise<ProcessResponse> {
  if (!res.ok) {
    let detail = res.statusText;
    try {
      detail = (await res.json()).detail ?? detail;
    } catch {
      /* ignore */
    }
    throw new Error(detail);
  }
  return res.json();
}

export function fetchDemo(): Promise<ProcessResponse> {
  return fetch(`${API_BASE}/api/demo`).then(handle);
}

export function processGmail(
  accessToken: string,
  maxResults = 15,
  query = "in:inbox",
): Promise<ProcessResponse> {
  return fetch(`${API_BASE}/api/gmail/process`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ access_token: accessToken, max_results: maxResults, query }),
  }).then(handle);
}
