from typing import Dict
from uuid import uuid4

from gwa_framework.resource.base import BaseResource
from gwa_framework.utils.decorators import validate_schema

from src.cache import cache
from src.database import master_async_session, read_replica_async_session
from src.models import StudentModel
from src.schemas import StudentInputSchema, StudentOutputSchema


class StudentResource(BaseResource):
    cache = cache
    method_decorators = {
        'create': [validate_schema(StudentInputSchema)],
        'update': [validate_schema(StudentInputSchema)],
    }

    def create(self, request_model: 'StudentInputSchema') -> Dict:
        student = StudentModel()
        student.id = request_model.student_id or str(uuid4())
        student.goal_id = request_model.goal_id
        student.weight = request_model.weight
        student.height = request_model.height
        student.current_gym_id = request_model.current_gym_id
        with master_async_session() as session:
            session.add(student)
            output = StudentOutputSchema()
            output.student_id = student.id
            output.goal_id = student.goal_id
            output.weight = student.weight
            output.height = student.height
            output.current_gym_id = student.current_gym_id
            output.validate()
            return output.to_primitive()

    def update(self, request_model: 'StudentInputSchema', student_id=None):
        student = StudentModel()
        student.id = student_id
        student.goal_id = request_model.goal_id
        student.weight = request_model.weight
        student.height = request_model.height
        student.current_gym_id = request_model.current_gym_id
        with master_async_session() as session:
            session.merge(student)
            output = StudentOutputSchema()
            output.student_id = student.id
            output.goal_id = student.goal_id
            output.weight = student.weight
            output.height = student.height
            output.current_gym_id = student.current_gym_id
            output.validate()
            return output.to_primitive()

    def list(self, args=None, kwargs=None):
        with read_replica_async_session() as session:
            results = []
            for student in session.query(StudentModel).all():
                output = StudentOutputSchema()
                output.student_id = student.id
                output.goal_id = student.goal_id
                output.weight = student.weight
                output.height = student.height
                output.current_gym_id = student.current_gym_id
                output.validate()
                results.append(output.to_primitive())
        return results

    def retrieve(self, student_id):
        with read_replica_async_session() as session:
            student = session.query(StudentModel).filter_by(id=student_id).first()
            output = StudentOutputSchema()
            output.student_id = student.id
            output.goal_id = student.goal_id
            output.weight = student.weight
            output.height = student.height
            output.current_gym_id = student.current_gym_id
            output.validate()
            return output.to_primitive()

    def destroy(self, student_id):
        with master_async_session() as session:
            session.query(StudentModel).filter_by(id=student_id).delete()
            return None


resources_v1 = [
    {'resource': StudentResource, 'urls': ['/students/<student_id>'], 'endpoint': 'Students StudentId',
     'methods': ['GET', 'PUT', 'PATCH', 'DELETE']},
    {'resource': StudentResource, 'urls': ['/students'], 'endpoint': 'Students',
     'methods': ['POST', 'GET']},
]
