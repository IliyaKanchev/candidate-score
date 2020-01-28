
import csv


def fill_from_csv(db_man, csv_path):
    with open(csv_path, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = -1

        for row in csv_reader:
            line_count += 1

            if line_count == 0:
                continue

            existing = db_man.search_candidate(row["candidate_ref"])

            if existing:
                candidate = existing[0]

            else:
                candidate = db_man.add_candidate(row["candidate_ref"], row["name"])

            # print(candidate.scores)

            db_man.add_score(candidate, row["score"])

            # print(candidate.scores)
            # print("# ref: %s, name: %s, score: %s" % (row["candidate_ref"], row["name"], row["score"]))

    db_man.commit()


def dump_csv_from_json(json_path, csv_path):
    pass
