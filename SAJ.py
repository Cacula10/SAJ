import pyodbc
# Repositório de variáveis
outros_num=[]
nunaoformato=[]
# conexão a base de dados
conn = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=10.100.188.129\ISAJ01;"
    "Database=SPJHML;"
    "uid=saj;pwd=nltrecRephlcrA"
)
# Criação do cursor para busca do processo
cursor = conn.cursor()
cursor2 = conn.cursor()

# Guardando as variaveis e concatenando para uso do like no banco
proc = str(input('Digite um numero para busca: '))
proc = '%' + proc + '%'

# Select's do Banco
cursor.execute("SELECT A.NUNAOFORMATADO, A.CDUSUINCLUSAO, B.CDPROCESSO, B.NUPROCESSO FROM SAJ.ESPJPROCOUTROSNUM AS A JOIN SAJ.ESPJPROCESSO AS B ON A.CDPROCESSO = B.CDPROCESSO WHERE A.NUNAOFORMATADO LIKE ?",proc)
for row in cursor:
    outros_num.append(row)
cursor2.execute("SELECT * FROM ESPJPROCESSO WHERE NUNAOFORMATADO LIKE ?",proc)
for row in cursor2:
    nunaoformato.append(row)

print()
print("Segue abaixo os processos encontrados")
print()
# Exibição ao usuário
print(f'Foram encontrado {len(outros_num)} processos')
print()
print('Cod')
for row in outros_num:
    print(row[0])
print()
continua = str(input("Deseja continuar? [S/N]"))[0].upper()
if continua == 'S':
    print("Segue abaixo o restante dos processos")
    print()
    print(nunaoformato)
else:
    print("FIM")
