from __future__ import annotations

import os
from hashlib import sha1
from typing import Dict

from app.core.zodiac import infer_zodiac
from app.interfaces.schemas import InsightRequest, InsightResponse
from app.services.cache import DailyCache
from app.services.pseudo_llm import PseudoLLM
from app.utils.prompt import build_prompt


ZODIAC_RULES: Dict[str, str] = {
    "Aries": "Channel your bold energy into one meaningful action.",
    "Taurus": "Steady focus and comfort rituals anchor progress.",
    "Gemini": "Curiosity and clear words move things forward.",
    "Cancer": "Nurture boundaries; care begins with you.",
    "Leo": "Lead with warmth; celebrate small wins.",
    "Virgo": "Refine the process; tidy space clarifies mind.",
    "Libra": "Seek balance; a fair compromise unlocks momentum.",
    "Scorpio": "Embrace depth; transform tension into insight.",
    "Sagittarius": "Expand horizons; optimism fuels exploration.",
    "Capricorn": "Structure and discipline create calm progress.",
    "Aquarius": "Innovate kindly; community lifts ideas.",
    "Pisces": "Trust intuition; gentle pace reveals answers.",
}


class InsightService:
    def __init__(self) -> None:
        self.cache = DailyCache()
        self.llm = PseudoLLM()

    @staticmethod
    def _user_key(req: InsightRequest) -> str:
        raw = f"{req.name}|{req.birth_date}|{req.birth_time}|{req.birth_place}"
        return sha1(raw.encode()).hexdigest()

    def generate_insight(self, req: InsightRequest) -> InsightResponse:
        language = (req.language or "en").lower()
        user_key = self._user_key(req)
        cached = self.cache.get(user_key, variant=language)
        if cached:
            return InsightResponse(**cached)

        zodiac = infer_zodiac(req.birth_date)
        rule = ZODIAC_RULES.get(zodiac, "Stay present; kindness guides choices.")
        prompt = build_prompt(req.name, zodiac, rule, language)
        
        # Generate insight using language-aware LLM
        text = self.llm.generate(prompt)

        result = InsightResponse(zodiac=zodiac, insight=text, language=language)
        self.cache.set(user_key, variant=language, value=result.dict())
        return result


