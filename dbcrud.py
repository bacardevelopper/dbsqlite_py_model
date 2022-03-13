import sqlite3

# config
conn = sqlite3.connect('ma_base.db')
conn_sql = conn.cursor()

# insert_exemple = "INSERT INTO employe VALUES("+id_rdm+","+nom+","+prenom+","+str(email)+")"

# class


class Db_crud:
    def __init__(self) -> None:
        pass

    def create_table(self, sql_request):
        try:
            conn_sql.execute(sql_request)
            conn_sql.close()
        except sqlite3.IntegrityError as e:
            print(e)

    def insert_data(self, id_rdm, nom, prenom, email):

        try:
            request_insert = "INSERT INTO employe VALUES(?, ?, ?, ?)"
            conn_sql.execute(request_insert, (id_rdm, nom, prenom, email))
            conn.commit() # permet de sauvegarder les modification
            # conn_sql.close()
        except sqlite3.IntegrityError as e:
            print(e)

    def afficher_table(self):
        try:
            conn_sql.execute('SELECT * FROM employe')
            une_list = conn_sql.fetchall()

            for data in une_list:
                print(data)
        except sqlite3.IntegrityError as e:
            print(e)

    def closer():
        conn_sql.close()
