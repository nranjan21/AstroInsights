from pydantic import BaseModel, Field


class InsightRequest(BaseModel):
    name: str = Field(..., description="User name")
    birth_date: str = Field(..., description="Birth date in YYYY-MM-DD")
    birth_time: str | None = Field(None, description="Birth time in HH:MM (24h)")
    birth_place: str | None = Field(None, description="Place of birth")
    language: str | None = Field("en", description="Output language code, e.g., en or hi")


class InsightResponse(BaseModel):
    zodiac: str
    insight: str
    language: str


