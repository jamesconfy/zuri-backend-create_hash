import json
import csv
import hashlib
from obj import obj

global row_count
input = input("Enter the name of your CSV file: ")
output = input
input += ".csv"
output += f".output.csv"

with open(input, newline="") as f:
    reader = csv.DictReader(f, delimiter=' ', quotechar='|')
    row_count = sum(1 for _ in reader)

with open(input, newline="") as file, open(output, "w", newline="") as out:    
    reader = csv.DictReader(file, delimiter=',', quotechar='|')
    writer = csv.DictWriter(out, delimiter=',', quotechar='|', fieldnames=["Serial Number", "Filename", "UUID", "Hashed"])
    writer.writeheader()
    for row in reader:
        obj = obj
        obj["name"] = row["Filename"]
        obj["series_number"] = row["Serial Number"]
        # obj["description"] = row["Description"]
        obj["collection"]["id"] = row["UUID"]
        obj["series_total"] = row_count

        json_file = json.dumps(obj, sort_keys=True, indent=2)
        hashed = hashlib.sha256(json_file.encode("utf-8")).hexdigest()

        row["Hashed"] = hashed
        writer.writerow(row)