import csv

with open("convinience_store.csv") as f:
    csv_list = []

    for row in csv.reader(f):
        if "".join(row).isdecimal():
            csv_list.append(list(map(int, row)))
        else:
            csv_list.append(row)

print(csv_list)
    