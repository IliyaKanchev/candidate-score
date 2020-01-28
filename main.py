
import os

from libs import db
from libs import utility


class MainApplication(object):
    def __init__(self):
        self._db_path = os.path.join(os.path.dirname(__file__), "db.sql")
        self._csv_path = os.path.join(os.path.dirname(__file__), "data", "candidates.csv")
        self._json_path = os.path.join(os.path.dirname(__file__), "data", "candidates-new.json")

        # print(self._db_path)
        # print(self._csv_path)
        # print(self._json_path)

        self._db_man = db.DbManager(db_path=self._db_path, echo=True)

    def main(self):
        utility.fill_from_csv(self._db_man, self._csv_path)
        utility.dump_csv_from_json(self._json_path, self._csv_path)


def main():
    app = MainApplication()
    app.main()


if __name__ == '__main__':
    main()
