import json

with open(r"movies\index.json") as file_op:
    data = json.load(file_op)

    for i in data:
        print(i)
