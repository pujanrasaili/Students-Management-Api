from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from models import db, Student

students_bp = Blueprint('students', __name__)

@students_bp.route('/api/students', methods=['GET'])
@jwt_required()
def get_students():
    search = request.args.get('search', '')
    course = request.args.get('course', '')
    query = Student.query
    if search:
        query = query.filter(
            (Student.first_name.ilike(f'%{search}%')) |
            (Student.last_name.ilike(f'%{search}%')) |
            (Student.student_id.ilike(f'%{search}%'))
        )
    if course:
        query = query.filter(Student.course.ilike(f'%{course}%'))
    students = query.all()
    return jsonify({'students': [s.to_dict() for s in students], 'total': len(students)}), 200

@students_bp.route('/api/students/<int:id>', methods=['GET'])
@jwt_required()
def get_student(id):
    student = Student.query.get_or_404(id)
    return jsonify(student.to_dict()), 200

@students_bp.route('/api/students', methods=['POST'])
@jwt_required()
def add_student():
    data = request.get_json()
    if Student.query.filter_by(student_id=data['student_id']).first():
        return jsonify({'message': 'Student ID already exists'}), 400
    student = Student(**data)
    db.session.add(student)
    db.session.commit()
    return jsonify({'message': 'Student added', 'student': student.to_dict()}), 201

@students_bp.route('/api/students/<int:id>', methods=['PUT'])
@jwt_required()
def update_student(id):
    student = Student.query.get_or_404(id)
    data = request.get_json()
    for key, value in data.items():
        setattr(student, key, value)
    db.session.commit()
    return jsonify({'message': 'Student updated', 'student': student.to_dict()}), 200

@students_bp.route('/api/students/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_student(id):
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    return jsonify({'message': 'Student deleted'}), 200

@students_bp.route('/api/students/stats', methods=['GET'])
@jwt_required()
def get_stats():
    total = Student.query.count()
    avg_gpa = db.session.query(db.func.avg(Student.gpa)).scalar() or 0
    courses = db.session.query(Student.course, db.func.count(Student.id)).group_by(Student.course).all()
    return jsonify({
        'total_students': total,
        'average_gpa': round(avg_gpa, 2),
        'students_per_course': {c: n for c, n in courses}
    }), 200