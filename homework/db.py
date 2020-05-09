import psycopg2
#import MySQLdb
import sqlite3


def test():
    for p in cursor.execute(f"SELECT * FROM patients where rowid=3"):
        print(type(p))
        return p


conn = sqlite3.connect("Covid.db")  # или :memory: чтобы сохранить в RAM
cursor = conn.cursor()

#conn = MySQLdb.connect('localhost', 'covid', '12345', 'Patients')
#conn = psycopg2.connect(dbname='patients', user='covid ',password='', host='localhost', port='5432')


cursor.execute("""
CREATE TABLE IF NOT EXISTS patients (
   first_name varchar(15),
   last_name varchar(15),
   birth_date char(10),
   phone char(16),
   document_type varchar(19),
   document_id varchar(12),
   PRIMARY KEY (document_id)
)
""")

cursor.execute("""
           CREATE TABLE IF NOT EXISTS {0} (
              first_name varchar(15),
              last_name varchar(15),
              birth_date char(10),
              phone char(16),
              document_type varchar(19),
              document_id varchar(12),
              PRIMARY KEY (document_id)
           )
           """.format('patients'))

cursor.execute("INSERT INTO patients VALUES ('Иван','Иванов','1990-12-12','+7-910-910-10-10','паспорт','0000 000001')")
conn.commit()

#cursor.execute("select * from patient")
cursor.execute(f"SELECT * FROM patients")
print(test())
print(test())
print(test())
#row = cursor.fetchall()
#for r in row:
#    print(r)
#print(row)
#conn.commit()
#cursor.execute('select * from patietns')
#data = cursor.fetchall()

cursor.close()
conn.close()

#print(data)