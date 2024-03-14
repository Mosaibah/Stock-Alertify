""" Alert Model """
from sqlalchemy import Column, String, Float, Date
from sqlalchemy.dialects.postgresql import UUID
from db.models.model_base import Base
from datetime import datetime
import uuid


class Alert(Base):
    __tablename__ = "alerts"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    threshold_price = Column(Float, nullable=False)
    symbol = Column(String, nullable=False)
    created_at = Column(Date, nullable=False, default=datetime.now())
