from enum import Enum
from typing import List

from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session

from app.db.database import Base, SessionLocal, engine
from app.models.translation import Translation
from app.services.translator import Audience, translate_text

# Create tables on startup (MVP approach)
Base.metadata.create_all(bind=engine)


class TranslateRequest(BaseModel):
    text: str = Field(..., min_length=1, description="Technical text to translate.")
    audience: Audience = Field(..., description="Target stakeholder audience.")


class TranslateResponse(BaseModel):
    audience: Audience
    summary: str
    risks: List[str]
    recommended_actions: List[str]


class HistoryItem(BaseModel):
    id: int
    audience: str
    input_text: str
    summary: str
    risks: List[str]
    recommended_actions: List[str]
    created_at: str


app = FastAPI(title="Governance Translator API")

# CORS (local dev)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/translate", response_model=TranslateResponse)
def translate(req: TranslateRequest, db: Session = Depends(get_db)):
    result = translate_text(req.text, req.audience)

    # Save to SQLite
    row = Translation(
        audience=result["audience"].value,
        input_text=req.text,
        summary=result["summary"],
        risks="\n".join(result["risks"]),
        recommended_actions="\n".join(result["recommended_actions"]),
    )
    db.add(row)
    db.commit()
    db.refresh(row)

    return result


@app.get("/history", response_model=List[HistoryItem])
def history(limit: int = 10, db: Session = Depends(get_db)):
    rows = (
        db.query(Translation)
        .order_by(Translation.created_at.desc())
        .limit(limit)
        .all()
    )

    items: List[HistoryItem] = []
    for r in rows:
        items.append(
            HistoryItem(
                id=r.id,
                audience=r.audience,
                input_text=r.input_text,
                summary=r.summary,
                risks=r.risks.splitlines(),
                recommended_actions=r.recommended_actions.splitlines(),
                created_at=r.created_at.isoformat(),
            )
        )
    return items

