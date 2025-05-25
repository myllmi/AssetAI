interface BodyResponse {
  code: number;
  message: string;
}

export interface LLMResponse extends BodyResponse {
  data: {
    llm: string
  }
}
