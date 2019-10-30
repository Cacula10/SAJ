import pyodbc
from collections import defaultdict

lista_SQL = []
dicionario_proc = defaultdict(list)
prossiga = 'S'

cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'preto_branco':'\033[7;33m'}

conn = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=10.100.188.129\ISAJ01;"
    "Database=SPJHML;"
    "uid=saj;pwd=nltrecRephlcrA"
)

cursor = conn.cursor()

num = str(input('Digite um numero para busca: '))
num = '%' + num + '%'

cursor.execute("SELECT A.CDUSUINCLUSAO, A.NUNAOFORMATADO, B.NUNAOFORMATADO,"
                   " CAST(A.NUPROCESSO AS VARCHAR) AS PROCESSO"
                   " FROM ESPJPROCESSO AS A "
                   "LEFT JOIN ESPJPROCOUTROSNUM AS B "
                   "ON A.CDPROCESSO = B.CDPROCESSO"
                   " WHERE NUPROCESSO LIKE ? "
                   "OR A.NUNAOFORMATADO LIKE ? "
                   "OR B.NUNAOFORMATADO LIKE ? ", num, num, num)

for row in cursor:
    lista_SQL.append(row[0].rstrip())
    lista_SQL.append(row[1])
    lista_SQL.append(row[2])
    lista_SQL.append(row[3])


print(cores['azul'], '>=' * 35)
print('{:^70}'.format('CONFIRA A LISTAGEM'))
print(cores['azul'], '>=' * 35)

print(lista_SQL)