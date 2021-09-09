import csv, sqlite3
listDB = []
with open('db.csv', 'r', encoding='utf-8') as fin:
    data_db = csv.reader(fin, delimiter = ";")
    for row in data_db:
        listDB.append(tuple(row))
DB = sqlite3.connect('data.bd')

link = DB.cursor()
# link.execute('''CREATE TABLE IF NOT EXISTS human(
#    'Корпорация',
#    'Филиал',
#    'Бизнес-центр',
#    'Адрес бизнес-центра',
#    'Должность сотрудника',
#    'ФИО сотрудника',
#    'Телефон сотрудника', 
#    'Отдел', 
#    'Статус руководителя', 
#    'Документы', 
#    'Подпись сотрудника', 
#    'Подпись руководителя', 
#    'Реквизит отдела', 
#    'Реквизит бизнес-центра', 
#    'Реквизит филиала', 
#    'Реквизит корпорации');''')
# DB.commit()

# listDB.pop(0)
# link.executemany("INSERT INTO human VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", listDB)
# DB.commit()
corporations = link.execute('''SELECT Корпорация FROM human GROUP by Корпорация''').fetchall()
# for corp in corporations:
#     cDB = sqlite3.connect(f'''{corp[0]}.bd''')
#     cDB.close()    

DB.close()

