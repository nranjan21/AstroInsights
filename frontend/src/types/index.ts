export interface InsightRequest {
  name: string;
  birth_date: string;
  birth_time?: string;
  birth_place?: string;
  language?: string;
}

export interface InsightResponse {
  zodiac: string;
  insight: string;
  language: string;
}

export interface ZodiacInfo {
  name: string;
  symbol: string;
  element: string;
  dates: string;
  traits: string[];
  colors: string[];
}
