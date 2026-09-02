"""SQLAlchemy models

Import Base from app.db. Define: Job, Measurement, CutItem, Photo.
See the spec in the project notes; Alembic autogenerate reads whatever
is defined here.
"""
from datetime import date, datetime

from sqlalchemy import (
    BigInteger, CheckConstraint, DateTime, Date, 
    Identity, String, Text, func,
)
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base  # noqa: F401

STATUS_VALUES = ["quoted", "measured","scheduled", "ordered", "arrived", "in_progress", "completed", "cancelled"]
STATUSES_WITHOUT_DATE = ("quoted", "measured", "cancelled")

class Job(Base):
    __tablename__ = "job"

    id: Mapped[int] = mapped_column(BigInteger, Identity(), primary_key=True)
    client_name: Mapped[str] = mapped_column(String(120),nullable=False)
    address: Mapped[str] = mapped_column(Text,nullable=False)
    status: Mapped[str] = mapped_column(String(20),nullable=False)
    scheduled_date: Mapped[date | None] = mapped_column(Date, nullable=True, index=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now())
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)

    __table_args__ = (
        CheckConstraint(status.in_(STATUS_VALUES), name="status_valid"),
        CheckConstraint(status.in_(STATUSES_WITHOUT_DATE) | (scheduled_date.isnot(None)), name="scheduled_date_required"
    ),
    )
# TODO(josue): Measurement
# TODO(josue): CutItem
# TODO(josue): Photo
