from mysql import connector
from datetime import date

db = connector.connect(
    host='localhost',
    user='root',
    password='root'
)

crs = db.cursor()

execsql = lambda cmd, crs: crs.execute(cmd)

createdatabase = lambda name, crs: execsql(f'CREATE DATABASE {name};\n', crs)
createtable = lambda name, fields, crs: execsql(f'CREATE TABLE {name} ({fields});\n', crs)
insertinto = lambda table, fields, values, crs : execsql(f'INSERT INTO {table} ({fields}) VALUES ({values});\n', crs)
selectwhere = lambda table, fields, filter, crs: execsql(f'SELECT {fields} FROM {table} WHERE {filter};\n', crs)
select = lambda table, fields, crs: execsql(f'SELECT {fields} FROM {table};\n', crs)
deletewhere = lambda table, filter, crs: execsql(f'DELETE FROM {table} WHERE {filter};\n', crs)
usedb = lambda db, crs: execsql(f'USE {db};\n', crs)

createdatabase('q4_av2', crs)
usedb('q4_av2', crs)

createtable('USUARIOS', 'id INT NOT NULL AUTO_INCREMENT, nome VARCHAR(255), console VARCHAR(255), PRIMARY KEY (id)', crs)
createtable('JOGOS', 'id INT NOT NULL AUTO_INCREMENT, nome VARCHAR(255), data_lancamento DATE, PRIMARY KEY (id)', crs)

insertinto('USUARIOS', 'nome, console', '"Usuario Teste", "Console Teste"', crs)
insertinto('USUARIOS', 'nome, console', '"Usuario Teste 2", "Console Teste 2"', crs)
insertinto('JOGOS', 'nome, data_lancamento', f'"Jogo Teste", "2023-10-18"', crs)
insertinto('JOGOS', 'nome, data_lancamento', f'"Jogo Teste 2", "2023-10-19"', crs)

print(select('USUARIOS', '*', crs))
print(selectwhere('USUARIOS', '*', 'nome = "Usuario Teste"', crs))
print(select('JOGOS', '*'))
print(selectwhere('JOGOS', '*', 'nome = "Jogo Teste"', crs))

deletewhere('USUARIOS', 'nome = "Usuario Teste"', crs)
print(select('USUARIOS', '*', crs))
deletewhere('USUARIOS', 'nome = "Usuario Teste 2"', crs)
print(select('USUARIOS', '*', crs))
deletewhere('JOGOS', 'nome = "Jogo Teste"', crs)
print(select('JOGOS', '*', crs))
deletewhere('JOGOS', 'nome = "Jogo Teste 2"', crs)
print(select('JOGOS', '*', crs))
