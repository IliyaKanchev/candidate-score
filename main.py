
import os

from libs import db
from libs import view
from libs import utility


class MainApplication(object):
    def __init__(self):
        self._db_path = os.path.join(os.path.dirname(__file__), "db.sql")
        self._csv_path = os.path.join(os.path.dirname(__file__), "data", "candidates.csv")
        self._json_path = os.path.join(os.path.dirname(__file__), "data", "candidates.json")

        self._db_man = db.DbManager(db_path=self._db_path, echo=False)
        self._view = view.View(self._db_man, debug=False)

    def _print_db(self):
        for candidate in self._db_man.dump_all():
            for score in candidate.scores:
                print("# ref: %s, name: %s, score: %s" % (candidate.candidate_ref, candidate.name, score.score))

    def main(self):
        utility.fill_from_csv(self._db_man, self._csv_path)
        utility.dump_csv_from_json(self._json_path, self._csv_path)

        try:
            self._view.serv()
        except KeyboardInterrupt:
            pass

        self._print_db()


def main():
    app = MainApplication()
    app.main()


if __name__ == '__main__':
    main()
