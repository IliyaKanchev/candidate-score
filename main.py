
import os

from libs import db


class MainApplication(object):
    def __init__(self):
        self._db_path = os.path.join(os.path.dirname(__file__), "db.sql")

        print(self._db_path)

        self._db_man = db.DbManager(db_path=self._db_path, echo=True)

    def main(self):
        pass


def main():
    app = MainApplication()
    app.main()


if __name__ == '__main__':
    main()
