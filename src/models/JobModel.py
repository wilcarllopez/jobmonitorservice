# src/models/JobModel.py
from sqlalchemy.dialects.postgresql import UUID
from marshmallow import fields, Schema
import datetime
from . import db

class JobModel(db.Model):

    # table name
    __tablename__ = 'modulelogs_app'
    job_id = db.Column(UUID(as_uuid=True), primary_key=True, nullable=False)
    app_name = db.Column(db.String(128), nullable=False)
    state = db.Column(db.String(128), nullable=False)
    date_created = db.Column(db.String(128), nullable=False)

    # class constructor
    def __init__(self, data):
        """
        Class constructor
        """
        self.job_id = data.get('job_id')
        self.app_name = data.get('app_name')
        self.state = data.get('state')
        self.date_created = data.get('date_created')

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all_jobs():
        return JobModel.query.all()

    @staticmethod
    def get_one_job(id):
        return JobModel.query.get(id)

    def __repl__(self):
        return '<id {}>'.format(self.id)

class JobSchema(Schema):
    """
    User Schema
    """
    job_id = fields.UUID(required=True)
    app_name = fields.Str(required=True)
    state = fields.Str(required=True)
    date_created = fields.Str(required=True)
