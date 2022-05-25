import csv

HEADERS = ["id", "question_id", "etc"]

def get_all_answers(myfile):
    with open(myfile, "r") as file:
        reader = csv.DictReader(file, HEADERS)
        # [
        #     {
        #         "id": "1",
        #         "question_id": "4",
        #         "etc": "una alta"
        #     },
        #     {
        #         "id": "2",
        #         "question_id": "4",
        #         "etc": "chestii"
        #     }
        # ]
        return list(reader)

def delete_answer(myfile, answer_id):
    output = [dictionar for dictionar in get_all_answers() if int(dictionar["id"]) != answer_id]

    with open(myfile, "r") as file:
        writer = csv.DictWriter(file, HEADERS)
        writer.writeheader()
        writer.writerows(output)