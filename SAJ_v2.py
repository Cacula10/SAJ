import pyodbc
lista_SQL = []

conn = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=10.100.188.129\ISAJ01;"
    "Database=SPJUSP;"
    "uid=saj;pwd=nltrecRephlcrA"
)
cursor = conn.cursor()

num = str(input('Digite um numero para busca: '))
num = '%' + num + '%'

cursor.execute("SELECT CAST(A.NUPROCESSO AS VARCHAR), A.NUNAOFORMATADO, B.NUNAOFORMATADO"
                   " FROM ESPJPROCESSO AS A "
                   "LEFT JOIN ESPJPROCOUTROSNUM AS B "
                   "ON A.CDPROCESSO = B.CDPROCESSO "
                   "WHERE A.NUPROCESSO LIKE ? OR A.NUNAOFORMATADO LIKE ? OR B.NUNAOFORMATADO LIKE ? ", num, num, num)

for row in cursor:
    lista_SQL.append(row[0])
    lista_SQL.append(row[1])
    lista_SQL.append(row[2])

print('>=' * 35)
print('{:^70}'.format('CONFIRA A LISTAGEM'))
print('>=' * 35)

print(lista_SQL)

a = input('...')
