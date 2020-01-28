
import sqlalchemy
from sqlalchemy import orm
from sqlalchemy.ext import declarative

Base = declarative.declarative_base()


class Score(Base):
    __tablename__ = 'scores'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    candidate_ref = sqlalchemy.Column(sqlalchemy.String, sqlalchemy.ForeignKey('candidates.candidate_ref'))
    score = sqlalchemy.Column(sqlalchemy.Float)

    candidate = orm.relationship("Candidate", back_populates="scores")


class Candidate(Base):
    __tablename__ = 'candidates'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String)
    candidate_ref = sqlalchemy.Column(sqlalchemy.String)

    scores = orm.relation("Score", back_populates="candidate")


class DbManager(object):
    def __init__(self, db_path=":memory:", echo=False):
        self._engine = sqlalchemy.create_engine('sqlite:///%s' % db_path, echo=echo)
        self._session = orm.Session(bind=self._engine)

        Base.metadata.create_all(self._engine)

    def commit(self):
        self._session.commit()

    def search_candidate(self, candidate_ref):
        return self._session.query(Candidate).filter(Candidate.candidate_ref == candidate_ref).all()

        # candidates = []
        #
        # for c, s in self._session.query(Candidate, Score).filter(Candidate.candidate_ref == candidate_ref).all():
        #     candidates.append(c)
        #
        # return candidates

    def dump_all(self, order_by_name=False):
        return self._session.query(Candidate).order_by(Candidate.name).all()\
            if order_by_name else self._session.query(Candidate).all()

    def add_candidate(self, candidate_ref, name):
        candidate = Candidate(candidate_ref=str(candidate_ref), name=str(name))
        self._session.add(candidate)

        return candidate

    def add_score(self, candidate, score_val):
        score = Score(candidate_ref=str(candidate.candidate_ref), score=float(score_val))
        candidate.scores.append(score)

        return score
