from gwa_framework.schemas.base import BaseSchema
from schematics.types import StringType, FloatType


class StudentInputSchema(BaseSchema):
    student_id = StringType(required=False, serialized_name='studentId')
    goal_id = StringType(required=False, serialized_name='goalId')
    current_gym_id = StringType(required=False, serialized_name='currentGymId')
    weight = FloatType(required=True)
    height = FloatType(required=True)


class StudentOutputSchema(BaseSchema):
    student_id = StringType(required=True, serialized_name='studentId')
    goal_id = StringType(required=False, serialized_name='goalId')
    current_gym_id = StringType(required=False, serialized_name='currentGymId')
    weight = FloatType(required=False)
    height = FloatType(required=False)
