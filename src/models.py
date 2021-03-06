from uuid import uuid4

from gwa_framework.models.base import BaseModel
from sqlalchemy import Column, Float
from sqlalchemy.dialects.postgresql import UUID


class StudentModel(BaseModel):
    __tablename__ = 'students'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    goal_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    current_gym_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    weight = Column(Float(), nullable=True)
    height = Column(Float(), nullable=True)
