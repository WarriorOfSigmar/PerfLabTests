import json
import sys

tests_file_json = sys.argv[1]
values_file_json = sys.argv[2]

with open("tests.json") as tests_file:
    tests = json.load(tests_file)

with open("values.json") as values_file:
    values = json.load(values_file)


def set_value(id):
    for value in values["values"]:
        if value["id"] == id["id"]:
            return value["value"]


def get_values(x):
    if "values" in x:
        for j in range(len(x["values"])):
            get_values(x["values"][j])
    if "value" in x:
        while x["value"] == "":
            x["value"] = set_value(x)


for example in tests["tests"]:
    get_values(example)

with open("report.json", "w") as report_json:
    json.dump(tests, report_json, indent=0)
