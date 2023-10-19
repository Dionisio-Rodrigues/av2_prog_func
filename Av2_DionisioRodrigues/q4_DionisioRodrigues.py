from mysql import connector

db = connector.connect(
    host='localhost',
    user='root',
    password='root'
)

crs = db.cursor()

execsql = lambda cmd, crs: crs.execute(cmd)
results = lambda res: [print(x) for x in res]

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

select('USUARIOS', '*', crs)
results(crs.fetchall())
selectwhere('USUARIOS', '*', 'nome = "Usuario Teste"', crs)
results(crs.fetchall())
select('JOGOS', '*', crs)
results(crs.fetchall())
selectwhere('JOGOS', '*', 'nome = "Jogo Teste"', crs)
results(crs.fetchall())

deletewhere('USUARIOS', 'nome = "Usuario Teste"', crs)
select('USUARIOS', '*', crs)
results(crs.fetchall())
deletewhere('USUARIOS', 'nome = "Usuario Teste 2"', crs)
select('USUARIOS', '*', crs)
results(crs.fetchall())
deletewhere('JOGOS', 'nome = "Jogo Teste"', crs)
select('JOGOS', '*', crs)
results(crs.fetchall())
deletewhere('JOGOS', 'nome = "Jogo Teste 2"', crs)
select('JOGOS', '*', crs)
results(crs.fetchall())
