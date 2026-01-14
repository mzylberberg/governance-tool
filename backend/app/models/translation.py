from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String, Text

from app.db.database import Base


class Translation(Base):
    __tablename__ = "translations"

    id = Column(Integer, primary_key=True, index=True)
    audience = Column(String(20), nullable=False)
    input_text = Column(Text, nullable=False)
    summary = Column(Text, nullable=False)

    # Store lists as newline-separated text for MVP simplicity
    risks = Column(Text, nullable=False)
    recommended_actions = Column(Text, nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
