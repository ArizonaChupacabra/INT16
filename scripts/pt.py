import json


def to_json(path: str):
    inside_list = []
    global_dir = {"vulnerabilities": inside_list}
    with open(path, 'r') as r:
        data = json.load(r)

    for i in data["site"]:
        for k in i["alerts"]:
            inside_list.append({"name": k["name"], "count": k["count"]})

    with open("../JSON_files/pt.json", "w") as f:
        json.dump(global_dir, f, indent=2)


to_json('../JSON_files/ZAP-Report-.json')
