
import flask


class View(object):
    def __init__(self, db_man):
        self._db_man = db_man
        self._app = flask.Flask(__name__)

        self._app.add_url_rule('/', 'index', view_func=self._index)
        self._app.add_url_rule('/candidates', 'candidates', view_func=self._candidates)

    def _index(self):
        return "Hello, World!"

    def _candidates(self):
        rows = ["<ul>"]

        for candidate in self._db_man.dump_all(True):
            rows.append("<li>%s" % candidate.name)
            rows.append("<ul>")

            for score in sorted(candidate.scores, key=lambda x: x.score):
                rows.append("<li>")
                rows.append("score: %s" % score.score)
                rows.append("</li>")

            rows.append("</ul>")
            rows.append("</li>")

        rows.append("</ul>")

        return "".join(rows)

    def serv(self):
        self._app.run(debug=True)
