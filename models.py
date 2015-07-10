import datetime as dt
from app import db
from flask.ext.login import UserMixin

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
        return '<Survey {}>'.format(self.id)

class Question(db.Model):
    __tablename__ = 'question'

    id = db.Column(db.Integer, primary_key=True, index=True)
    question_en = db.Column(db.String(255))
    question_es = db.Column(db.String(255))
    question_type = db.Column(db.String(255))
    survey_id = db.Column(db.Integer, db.ForeignKey('survey.id'))

    def __init__(self, question_en, question_es, question_type, survey_id):
        self.question_en = question_en
        self.question_es = question_es
        self.question_type = question_type
        self.survey_id = survey_id

    def __repr__(self):
        return '<Question {0}, {1}>'.format(self.id, self.survey_id)

class User(db.Model, UserMixin):
    __tablename__ = 'user'

    email = db.Column(db.String(80), primary_key=True, nullable=False, index=True)
    created_at = db.Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)
    first_name = db.Column(db.String(30), nullable=True)
    last_name = db.Column(db.String(30), nullable=True)
    active = db.Column(db.Boolean(), default=True)

    @property
    def full_name(self):
        return "{0} {1}".format(self.first_name, self.last_name)

    def __repr__(self):
        return '<User({email!r})>'.format(email=self.email)

    def get_id(self):
        return self.email
