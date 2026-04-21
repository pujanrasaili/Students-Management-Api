import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'pujan-secret-key-2024'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///students.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'jwt-secret-key-2024'