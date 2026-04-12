import json

def load_and_prepare_data(file_path):
    with open(file_path, 'r') as file:
        dat = json.load(file)

    for i in dat:
        a, b = i["start"].split(":")
        i["start_min"] = int(a) * 60 + int(b)

        a, b = i["end"].split(":")
        i["end_min"] = int(a) * 60 + int(b)

    dat.sort(key=lambda r: r["start_min"])

    return dat


if __name__ == "__main__":
    dat = load_and_prepare_data("data/sample_route.json")

    # Debug print
    print("Prepared Data:")
    for r in dat:
        print(r)
