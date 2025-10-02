import argparse
import json
from app.interfaces.schemas import InsightRequest
from app.services.insight_service import InsightService


def main():
    parser = argparse.ArgumentParser(description="Astrological Insight Generator CLI")
    parser.add_argument("--name", required=True)
    parser.add_argument("--birth_date", required=True, help="YYYY-MM-DD")
    parser.add_argument("--birth_time", default=None, help="HH:MM 24h")
    parser.add_argument("--birth_place", default=None)
    parser.add_argument("--language", default="en", choices=["en", "hi"])
    args = parser.parse_args()

    service = InsightService()
    req = InsightRequest(
        name=args.name,
        birth_date=args.birth_date,
        birth_time=args.birth_time,
        birth_place=args.birth_place,
        language=args.language,
    )
    res = service.generate_insight(req)
    print(json.dumps(res.dict(), ensure_ascii=False))


if __name__ == "__main__":
    main()


