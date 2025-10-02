from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Prompt:
    system: str
    user: str


def build_prompt(name: str, zodiac: str, rule_of_day: str, language: str) -> Prompt:
    system = (
        "You are an astrological guide generating concise, kind, practical daily insights."
    )
    user = (
        f"User: {name}\n"
        f"Zodiac: {zodiac}\n"
        f"Guidance: {rule_of_day}\n"
        f"Language: {language}\n"
        "Respond with a single 1-2 sentence insight."
    )
    return Prompt(system=system, user=user)


