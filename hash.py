import json
import csv
import hashlib
from obj import obj

global row_count
input = input("Enter the name of your CSV file: ")
output = input
output_json = input
input += ".csv"
output += f".output.csv"
output_json += ".json"

with open(input, newline="") as f:
    reader = csv.DictReader(f, delimiter=' ', quotechar='|')
    row_count = sum(1 for _ in reader)

with open(input, newline="") as file, open(output, "w", newline="") as out, open(output_json, "w") as outfile:    
    reader = csv.DictReader(file, delimiter=',', quotechar='|')
    writer = csv.DictWriter(out, delimiter=',', quotechar='|', fieldnames=["Serial Number", "Filename", "UUID", "Hashed"])
    writer.writeheader()
    for row in reader:
        obj = obj
        obj["name"] = row["Filename"] if row["Filename"] else ""
        obj["series_number"] = row["Serial Number"] if row["Serial Number"] else ""
        # obj["description"] = row["Description"] if row["Description"] else ""
        # obj["attributes"][0]["value"] = row["Gender"] if row["Gender"] else ""
        obj["collection"]["id"] = row["UUID"] if row["UUID"] else ""
        obj["series_total"] = row_count

        json_file = json.dumps(obj, sort_keys=True, indent=2)
        hashed = hashlib.sha256(json_file.encode("utf-8")).hexdigest()

        
        row["Hashed"] = hashed
        writer.writerow(row)
        outfile.write(json_file)