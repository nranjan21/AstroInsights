# Backend - Astrological Insight Generator

FastAPI backend service for generating personalized astrological insights.

## 🚀 Quick Start

```bash
# Create virtual environment
python -m venv .venv
.venv\Scripts\activate  # Windows PowerShell: .venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Start the server
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## 📁 Project Structure

```
app/
├── core/               # Core business logic
│   └── zodiac.py      # Zodiac sign inference
├── services/          # Service layer
│   ├── insight_service.py    # Main insight generation
│   ├── pseudo_llm.py         # Text generation engine
│   ├── translation.py        # Multi-language support
│   └── cache.py             # Daily caching
├── interfaces/        # API contracts
│   └── schemas.py     # Pydantic models
├── utils/             # Utilities
│   └── prompt.py      # Prompt building
└── main.py           # FastAPI application
```

## 🔧 API Endpoints

### Health Check
```
GET /health
```

### Generate Insight
```
POST /predict
Content-Type: application/json

{
  "name": "Ritika",
  "birth_date": "1995-08-20",
  "birth_time": "14:30",
  "birth_place": "Jaipur, India",
  "language": "en"
}
```

### API Documentation
Visit `http://localhost:8000/docs` for interactive Swagger documentation.

## 🎯 Features

- **Zodiac Inference**: Determines zodiac sign from birth date
- **Personalized Insights**: 3 unique insights per zodiac sign
- **Multi-language**: English and Hindi support
- **Daily Caching**: In-memory cache for performance
- **CLI Interface**: Command-line tool for quick access
- **CORS Enabled**: Ready for frontend integration

## 🛠️ CLI Usage

```bash
python cli.py --name "Ritika" --birth_date "1995-08-20" --birth_time "14:30" --birth_place "Jaipur, India" --language en
```

## 📦 Dependencies

- `fastapi` - Web framework
- `uvicorn[standard]` - ASGI server
- `pydantic>=2` - Data validation
- `python-dateutil` - Date parsing

## 🔄 Architecture

The backend follows a clean architecture pattern:

1. **Core Layer**: Pure business logic (zodiac inference)
2. **Service Layer**: Application services (insights, caching, translation)
3. **Interface Layer**: API contracts and data models
4. **Utils Layer**: Shared utilities and helpers

## 🌍 Multi-language Support

- **English**: Default language with zodiac-specific insights
- **Hindi**: Complete Hindi translations for all zodiac signs

## 🚀 Deployment

The backend is ready for deployment on any platform that supports Python:

- **Local Development**: `uvicorn app.main:app --reload`
- **Production**: `uvicorn app.main:app --host 0.0.0.0 --port 8000`
- **Docker**: Can be containerized easily
- **Cloud Platforms**: Compatible with Heroku, Railway, etc.

## 🔧 Configuration

No environment variables required - the service uses sensible defaults and works out of the box.
