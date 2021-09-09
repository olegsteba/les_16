import csv, sqlite3
listDB = []
with open('db.csv', 'r', encoding='utf-8') as fin:
    data_db = csv.reader(fin, delimiter = ";")
    for row in data_db:
        listDB.append(tuple(row))

print(listDB)