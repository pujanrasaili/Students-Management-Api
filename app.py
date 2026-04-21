from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from flasgger import Swagger
from config import Config
from models import db
from auth import auth_bp
from routes import students_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
jwt = JWTManager(app)

swagger_config = {
    "headers": [],
    "specs": [{"endpoint": "apispec", "route": "/apispec.json", "rule_filter": lambda rule: True, "model_filter": lambda tag: True}],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/docs"
}
swagger = Swagger(app, config=swagger_config)

app.register_blueprint(auth_bp)
app.register_blueprint(students_bp)

@app.route('/')
def index():
    return jsonify({
        'message': 'Student Management API',
        'author': 'Pujan Rasaili | Bedfordshire University',
        'version': '1.0',
        'docs': '/docs',
        'endpoints': {
            'register': 'POST /api/register',
            'login': 'POST /api/login',
            'students': 'GET/POST /api/students',
            'student': 'GET/PUT/DELETE /api/students/<id>',
            'stats': 'GET /api/students/stats'
        }
    })

@app.errorhandler(404)
def not_found(e):
    return jsonify({'message': 'Resource not found'}), 404

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)