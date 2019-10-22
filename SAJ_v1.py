import pyodbc
from collections import defaultdict
# Repositório de variáveis

cont = 0
lista_SQL = []
dicionario_proc = defaultdict(list)

cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'preto_branco':'\033[7;33m'}

# conexão a base de dados
conn = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=10.100.188.129\ISAJ01;"
    "Database=SPJTESTE;"
    "uid=saj;pwd=nltrecRephlcrA"
)
# Criação do cursor para busca do processo
cursor = conn.cursor()

# Guardando as variaveis e concatenando para uso do like no banco
num = str(input('Digite um numero para busca: '))
num = '%' + num + '%'

# Select's do Banco
cursor.execute("SELECT CDUSUINCLUSAO, NUNAOFORMATADO, CAST(NUPROCESSO AS VARCHAR) AS PROCESSO "
               "FROM ESPJPROCESSO WHERE NUPROCESSO LIKE ? OR NUNAOFORMATADO LIKE ?", num, num)

for row in cursor:
    lista_SQL.append(row[0].rstrip())
    lista_SQL.append(row[1])
    lista_SQL.append(row[2])
    cont += 1

splited_list = int(len(lista_SQL)/3)
splited = []
len_lista_SQL = len(lista_SQL)
for i in range(splited_list):
    start = int(i*len_lista_SQL/splited_list)
    end = int((i+1) * len_lista_SQL/splited_list)
    splited.append(lista_SQL[start:end])

for usuario, numero, processo in splited:
    dicionario_proc[usuario].append((numero, processo))

print(dicionario_proc['3039753'])