import type { ProcessResponse } from "./types";

// Default to same-origin ("") so the app works when the backend serves it
// directly (the single-link iPad setup). For two separate dev servers, set
// VITE_API_BASE=http://localhost:8000 in frontend/.env.
const API_BASE = import.meta.env.VITE_API_BASE ?? "";

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
