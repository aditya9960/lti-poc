from marshmallow import fields, Schema
from app import db


class Student(db.Model):
    __tablename__ = 'student'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    rollno = db.Column(db.Integer, index=True, unique=True)
    division = db.Column(db.String(64), nullable=True)
    clas = db.Column(db.String(64), nullable=True)

    def __init__(self, data):
        self.name = data.get('name')
        self.rollno = data.get('rollno')
        self.division = data.get('division')
        self.clas = data.get('clas')

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_student_by_rollno(value):
      return Student.query.filter_by(rollno=value).first()

    @staticmethod
    def get_all_students():
        return Student.query.all()

class StudentSchema(Schema):
  id = fields.Int(dump_only=True)
  name = fields.Str(required=True)
  rollno = fields.Int(required=True)
  division = fields.Str(required=False)
  clas = fields.DateTime(required=False)
