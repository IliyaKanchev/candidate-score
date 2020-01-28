
import csv
import json


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

            if 0.0 <= float(row["score"]) <= 100.0:
                db_man.add_score(candidate, row["score"])

            # print(candidate.scores)
            # print("# ref: %s, name: %s, score: %s" % (row["candidate_ref"], row["name"], row["score"]))

    db_man.commit()


def dump_csv_from_json(json_path, csv_path):
    with open(json_path, mode='r') as json_file:
        json_object = json.load(json_file)

    json_object.sort(key=lambda x: x["score"])

    with open(csv_path, mode='w') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=['candidate_ref', 'name', 'score'])

        writer.writeheader()

        for dct in json_object:
            writer.writerow(dct)
