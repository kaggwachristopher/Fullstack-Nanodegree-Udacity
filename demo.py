import psycopg2

connection = psycopg2.connect(database="test_db",user="postgres")

cursor = connection.cursor()
cursor.execute('''
drop table if exists table2;
''')

cursor.execute('''
create table table2(
    id integer primary key,
    completed boolean not null default False
);
''')
cursor.execute('insert into table2 (id,completed) values (%s, %s)',(1,True))

sql = 'INSERT INTO table2 (id, completed) VALUES (%(id)s, %(completed)s);'

data = {
  'id': 2,
  'completed': False
}

cursor.execute(sql, data)

connection.commit()

connection.close()
cursor.close()