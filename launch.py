from dbcrud import Db_crud
import random
import string

# generer id
lettres = string.ascii_lowercase
id_rdm = ''.join(random.choice(lettres) for i in range(10))
# request
request_creat_table = '''
    CREATE TABLE employe(id_random varchar NOT NULL, nom varchar NOT NULL, prenom varchar NOT NULL, email varchar)
'''

# config and launch methods
db_main = Db_crud()
# db_main.create_table(request_creat_table)
email_recup = 'dato.banga.pro@gmail.com'
db_main.insert_data(id_rdm, 'bacar', 'darwin', email_recup)
db_main.recuperer_un('dahmwpnanu')
db_main.afficher_table()