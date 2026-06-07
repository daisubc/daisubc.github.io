export type Priority = "high" | "medium" | "low";

export interface ProcessedEmail {
  id: string;
  sender: string;
  subject: string;
  date: string;
  summary: string;
  priority: Priority;
  priority_score: number;
  category: string;
  action_required: boolean;
  reason: string;
}

export interface ProcessResponse {
  emails: ProcessedEmail[];
  llm_used: boolean;
  model: string | null;
}
