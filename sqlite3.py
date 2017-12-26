import sqlite3
vt = sqlite3.connect('utopian.sqlite')
sv = vt.cursor()
sv.execute("CREATE TABLE utopianio (isim, soyisim)")
veri_gir = """INSERT INTO utopianio VALUES ('Seyda', 'Bozkurt')"""
sv.execute(veri_gir)
sv.commit()
veriler = sv.fetchall()
print(veriler)
