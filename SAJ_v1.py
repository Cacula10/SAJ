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
    "Database=SPJTESTE;"
    "uid=saj;pwd=nltrecRephlcrA"
)

cursor = conn.cursor()

prossiga = 'S'
while prossiga == 'S':

    num = str(input('Digite um numero para busca: '))
    num = '%' + num + '%'

    cursor.execute("SELECT CDUSUINCLUSAO, NUNAOFORMATADO, CAST(NUPROCESSO AS VARCHAR) AS PROCESSO "
                   "FROM ESPJPROCESSO WHERE NUPROCESSO LIKE ? OR NUNAOFORMATADO LIKE ?", num, num)

    for row in cursor:
        lista_SQL.append(row[0].rstrip())
        lista_SQL.append(row[1])
        lista_SQL.append(row[2])

    splited_list = int(len(lista_SQL)/3)
    splited = []
    len_lista_SQL = len(lista_SQL)

    for i in range(splited_list):
        start = int(i*len_lista_SQL/splited_list)
        end = int((i+1) * len_lista_SQL/splited_list)
        splited.append(lista_SQL[start:end])

    for usuario, numero, processo in splited:
        dicionario_proc[usuario].append((numero, processo))
    print(cores['azul'], '>=' * 35)
    print('SEGUE LISTAGEM')
    print(cores['azul'], '>=' * 35)
    for k, v in dicionario_proc.items():
        print(cores['amarelo'], f'Usuário: {k}     Dados: {v}')

    prossiga = str(input('Deseja continuar [S/N]?')).upper()[0]

    if prossiga == 'N':
        print(cores['azul'], 'ESPERO QUE TENHA ENCONTRADO O PROCESSO')
        break
    elif prossiga not in 'SN':
        prossiga = str(input('Favor digitar [S] ou [N]'))
