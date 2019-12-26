import sqlite3

con=sqlite3.connect("database.db")

cursor=con.cursor()

def tablo_oluştur():
    cursor.execute("create table IF not EXISTS veriler(id INT ,key TEXT,value TEXT)")
def veri_ekle(gelen_key, gelen_value):
    # veriler="""INSERT INTO veriler VALUES (50,{},{})""".format(gelen_key,gelen_value)
    # cursor.execute(veriler)
    con.commit()
    con.close()

tablo_oluştur()
veri_ekle(50,555)
