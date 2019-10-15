import pyodbc

conn = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=10.100.188.129\ISAJ01;"
    "Database=SPJHML;"
    "uid=saj;pwd=nltrecRephlcrA"
)
cursor = conn.cursor()
proc = str( input( 'Informe o numero do processo: ' ) )
proc = '%' + proc + '%'
cursor.execute(
    "SELECT A.NUNAOFORMATADO, A.CDUSUINCLUSAO, B.CDPROCESSO, B.NUPROCESSO FROM SAJ.ESPJPROCOUTROSNUM AS A JOIN SAJ.ESPJPROCESSO AS B ON A.CDPROCESSO = B.CDPROCESSO WHERE A.NUNAOFORMATADO LIKE ?",
    proc)

for row in cursor:
    print(row)

a = str(input('='))