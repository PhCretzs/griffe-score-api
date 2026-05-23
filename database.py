#database.py
import sqlite3 

def get_db(): #conn com banco
    conn = sqlite3.connect("griffe_db.db") #abre conn
    
    conn.row_factory = sqlite3.Row # retornar linhas acessiveis por nome
    return conn