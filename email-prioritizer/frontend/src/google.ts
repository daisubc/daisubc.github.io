// Thin wrapper around Google Identity Services for an OAuth access token
// with gmail.readonly scope. Runs entirely in the browser; the token is sent
// to our backend per-request and never stored server-side.

const CLIENT_ID = import.meta.env.VITE_GOOGLE_CLIENT_ID ?? "";
const SCOPE = "https://www.googleapis.com/auth/gmail.readonly";

// Minimal typing for the GIS global injected by the gsi/client script.
interface TokenResponse {
  access_token: string;
  error?: string;
}
declare global {
  interface Window {
    google?: {
      accounts: {
        oauth2: {
          initTokenClient(config: {
            client_id: string;
            scope: string;
            callback: (resp: TokenResponse) => void;
          }): { requestAccessToken: () => void };
        };
      };
    };
  }
}

export const googleConfigured = (): boolean => CLIENT_ID.length > 0;

export function requestGmailToken(): Promise<string> {
  return new Promise((resolve, reject) => {
    if (!CLIENT_ID) {
      reject(new Error("VITE_GOOGLE_CLIENT_ID is not set."));
      return;
    }
    if (!window.google) {
      reject(new Error("Google Identity Services not loaded yet. Try again in a moment."));
      return;
    }
    const client = window.google.accounts.oauth2.initTokenClient({
      client_id: CLIENT_ID,
      scope: SCOPE,
      callback: (resp) => {
        if (resp.error || !resp.access_token) {
          reject(new Error(resp.error ?? "Authorization failed."));
        } else {
          resolve(resp.access_token);
        }
      },
    });
    client.requestAccessToken();
  });
}
