# src/models/JobModel.py
from marshmallow import fields, Schema
import datetime
from . import db
from .StateModel import StateSchema


class JobModel(db.Model):

    # table name
    __tablename__ = 'jobs'
    id = db.Column(db.Integer, primary_key=True)
    job_id = db.Column(UUID(as_uuid=True), unique=True, nullable=False)
    app_name = db.Column(db.String(128), nullable=False)
    state = db.relationship('StateModel', backref='users', lazy=True)
    date_created = db.Column(db.DateTime, nullable=False)
    #blogposts = db.relationship('BlogpostModel', backref='users', lazy=True)  # add this new line

    # class constructor
    def __init__(self, data):
        """
        Class constructor
        """
        self.job_id = data.get('job_id')
        self.app_name = data.get('app_name')
        self.state = self.__generate_hash(data.get('password'))
        self.created_at = datetime.datetime.utcnow()
        self.modified_at = datetime.datetime.utcnow()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        for key, item in data.items():
            setattr(self, key, item)
        self.modified_at = datetime.datetime.utcnow()
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all_users():
        return JobModel.query.all()

    @staticmethod
    def get_one_user(id):
        return JobModel.query.get(id)

    def __repr(self):
        return '<id {}>'.format(self.id)


class UserSchema(Schema):
    """
    User Schema
    """
    id = fields.Int(dump_only=True)
    job_id = fields.UUID(required=True)
    app_name = fields.Str(required=True)
    state = fields.Nested(StateSchema, many=True)
    password = fields.Str(required=True)
    date_created = fields.DateTime(required=True)
