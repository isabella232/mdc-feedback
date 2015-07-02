# import datetime
from app import db
from sqlalchemy.schema import Table

# https://pythonhosted.org/Flask-SQLAlchemy/models.html

class Survey(db.Model):
    __tablename__ = 'survey'

    id = db.Column(db.Integer, primary_key=True, index=True)
    title_en = db.Column(db.String(255))
    title_es = db.Column(db.String(255))
    description_en = db.Column(db.String(255))
    description_es = db.Column(db.String(255))
    questions = db.relationship('Question', backref='survey')

    def __init__(self, title_en, title_es, description_en, description_es):
        self.title_en = title_en
        self.title_es = title_es
        self.description_en = description_en
        self.description_es = description_es

    def __repr__(self):
        return '<id {}>'.format(self.id)

class Question(db.Model):
    __tablename__ = 'question'

    id = db.Column(db.Integer, primary_key=True, index=True)
    question_en = db.Column(db.String(255))
    question_es = db.Column(db.String(255))
    question_type = db.Column(db.String(255))
    survey_id = db.Column(db.Integer, db.ForeignKey('survey.id'))

    def __init__(self, question_en, question_es, question_type):
        self.question_en = question_en
        self.question_es = question_es
        self.question_type = question_type

    def __repr__(self):
        return '<id {}>'.format(self.id)

