# Importar csv
import csv
# Importa a função escape para garantir a leitura de caracteres especiais de fomra segura
from html import escape

#Importar o CSV

with open("alunos.csv",encoding="UTF-8-sig") as ficheiro:

    #le os dados do csv e guarda numa lista
    alunos=list(csv.DictReader(ficheiro))
#Criar o documento HTML

html="""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Documento gerado por python</title>
</head>

<body>
    <h1>Lista de alunos</h1>
    <table border="1">
        <tr>
            <th>Nome</th>
            <th>Idade</th>
            <th>Curso</th>
            <th>Nota</th>
        </tr>
"""

#Acrescentar os dados a tabela HTML
#percorrer todos os alunosda lista
for aluno in alunos:
    html+=f"""
        <tr>
            <td>{escape(aluno['Nome'])}</td>
            <td>{escape(aluno['Idade'])}</td>
            <td>{escape(aluno['Curso'])}</td>
            <td>{escape(aluno['Nota'])}</td>
        </tr>


    """

html+="""
    </table>
</body>

</html>

"""

with open("gerar.html","w",encoding="UTF-8-sig") as ficheiro:
    ficheiro.write(html)
print("Ficheiro criado com sucesso!")