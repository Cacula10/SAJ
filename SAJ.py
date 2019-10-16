import pyodbc
import time

# Repositório de variáveis
outros_num=[]
nunaoformato=[]
n_list=[]

cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'preto_branco':'\033[7;33m'}

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
time.sleep(0.5)

# Select's do Banco
cursor.execute("SELECT A.NUNAOFORMATADO, A.CDUSUINCLUSAO, CAST(B.NUPROCESSO AS VARCHAR) AS PROCESSO FROM SAJ.ESPJPROCOUTROSNUM AS A JOIN SAJ.ESPJPROCESSO AS B ON A.CDPROCESSO = B.CDPROCESSO WHERE A.NUNAOFORMATADO LIKE ?",proc)
for row in cursor:
    outros_num.append(row)
    outros_num.append(row[1].strip())
    n_list.append(outros_num[0][0])
    n_list.append(outros_num[0][2])
    n_list.append(outros_num[1])

cursor2.execute("SELECT * FROM ESPJPROCESSO WHERE NUNAOFORMATADO LIKE ?",proc)
for row in cursor2:
    nunaoformato.append(row)
print(format(cores['azul']))
print(("=>" * 20).format(""))
print('PROCURANDO')
print(("=>" * 20).format(""))
print(format(cores['limpa']))
time.sleep(2)
print(f'ENCONTRADO {len(outros_num)} PROCESSO(s)')
print()

#  Exibição do usuário

print(n_list)

continua = str(input("Deseja continuar? [S/N]"))[0].upper()
if continua == 'S':
    print("Segue abaixo o restante dos processos")
    print()
    print(nunaoformato)
else:
    print("FIM")