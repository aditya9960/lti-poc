from flask import request, json, Response
from . import mod_student
from .models import Student, StudentSchema
from app.main import main
from app import db
student_schema = StudentSchema()


@mod_student.route('/create',methods=['POST'])
def create():
    """
    create student
    """
    req_data = request.get_json()
    data, error = user_schema.load(req_data)

    if error:
        import pdb;pdb.set_trace();
        print("error fiels ")
        return custom_response(error, 400)

    student_exists = Student.get_student_by_rollno(data.get('rollno'))
    if student_exists:
        import pdb;pdb.set_trace();
        print("error student_exists")
        return custom_response({'error': 'Student with this rollno exists'}, 400)

    student = Student(data)
    student.save()
    student_data = student_schema.dump(student).data
    return custom_response({'rollno': student_data.get('rollno')}, 201)


@mod_student.route('/', methods=['GET'])
def get_all():
    """
    get all studs
    """
    students = Student.get_all_students()
    student_data = student_schema.dump(students, many=True).data
    return custom_response(student_data, 201)


def custom_response(res, status_code):
    """
    Custom Response Function
    """
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
        status=status_code
    )