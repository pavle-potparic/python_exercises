import json

file = "json_example.json"
with open(file, "r", encoding="utf-8") as load_file:
    data = json.load(load_file)
    accounting = data["accounting"]
    sales = data["sales"]
    print(accounting)
    print(sales)
