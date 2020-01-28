
import sqlalchemy
from sqlalchemy import orm
from sqlalchemy.ext import declarative

Base = declarative.declarative_base()


class Score(Base):
    __tablename__ = 'scores'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    candidate_ref = sqlalchemy.Column(sqlalchemy.String, sqlalchemy.ForeignKey('candidates.candidate_ref'))
    score = sqlalchemy.Column(sqlalchemy.Float)

    user = orm.relationship("Candidate", back_populates="scores")


class Candidate(Base):
    __tablename__ = 'candidates'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String)
    candidate_ref = sqlalchemy.Column(sqlalchemy.String)
    scores = orm.relation("Score", back_populates="candidates")


class DbManager(object):
    def __init__(self, db_path="/:memory:", echo=False):
        self._engine = sqlalchemy.create_engine('sqlite://%s' % db_path, echo=echo)
        self._session = orm.sessionmaker(bind=self._engine)

        Base.metadata.create_all(self._engine)

    def commit(self):
        self._session.commit()

    def insert(self, candidate):
        self._session.add(candidate)
        self.commit()
