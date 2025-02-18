import csv

data = [
    {"username": "laroes", "color": "blue"},
    {"username": "a", "color": "a"},
    {"username": "b", "color": "b"},
    {"username": "c", "color": "c"},
    {"username": "d", "color": "d"},
    {"username": "e", "color": "e"},
    {"username": "f", "color": "f"},
    {"username": "g", "color": "g"},
    {"username": "h", "color": "h"},
    {"username": "i", "color": "i"},
    {"username": "j", "color": "j"},
    {"username": "k", "color": "k"},
    {"username": "l", "color": "l"},
    {"username": "m", "color": "m"},
    {"username": "n", "color": "n"},
    {"username": "o", "color": "o"},
    {"username": "p", "color": "p"},
    {"username": "q", "color": "q"},
    {"username": "r", "color": "r"},
    {"username": "s", "color": "s"},
    {"username": "t", "color": "t"},
    {"username": "u", "color": "u"},
    {"username": "v", "color": "v"},
    {"username": "w", "color": "w"},
    {"username": "x", "color": "x"},
    {"username": "y", "color": "y"},
    {"username": "z", "color": "z"},
]

items = [
    []
]



with open('Notes/write to notes/WriteTo.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["new_user", "black"])

with open('Notes/write to notes/WriteTo.csv', 'w', newline='') as file:
    fieldnames = ["username", "color"]
    writer = csv.DictWriter(file, fieldnames= fieldnames)
    writer.writeheader()
    writer.writerows(data)

with open('Notes/write to notes/WriteTo.csv', 'a', newline='') as file:
    fieldnames = ["username", "color"]
    writer = csv.DictWriter(file, fieldnames= fieldnames)
    writer.writeheader()
    writer.writerows(data)

with open('Notes/write to notes/WriteTo.csv', 'w', newline='') as file:
    fieldnames = ["username", "color"]
    writer = csv.DictWriter(file, delimiter="|", fieldnames= fieldnames)
    writer.writeheader()
    writer.writerows(data)


with open('Notes/write to notes/WriteTo.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print("username:", row[0], "     password:", row[1])