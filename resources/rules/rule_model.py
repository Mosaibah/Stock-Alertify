""" Alert Rule Model """
from sqlalchemy import Column, String, Float, Date, BOOLEAN
from sqlalchemy.dialects.postgresql import UUID
from db.models.model_base import Base
from datetime import datetime
import uuid


class Rule(Base):
    __tablename__ = "alert_rules"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    threshold_price = Column(Float, nullable=False)
    symbol = Column(String, nullable=False)
    is_deleted = Column(BOOLEAN, nullable=True)
    created_at = Column(Date, nullable=False, default=datetime.now())
