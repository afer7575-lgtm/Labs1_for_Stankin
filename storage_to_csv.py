import csv

def to_storage(data, file_name) -> None:
    path = f"storage/{file_name}.csv"

    fieldnames = set()
    for d in data:
        fieldnames.update(d.keys())
    fieldnames = sorted(fieldnames)
    with open(path,"w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)