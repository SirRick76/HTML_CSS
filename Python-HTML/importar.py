# Importar csv
import csv
# Importa a função escape para garantir a leitura de caracteres especiais de fomra segura
from html import escape
from pathlib import Path
#Importar o CSV
ficheiro_html=Path("importar.html")
with open("alunos.csv","r",encoding="UTF-8-sig") as ficheiro:

    #le os dados do csv e guarda numa lista
    alunos=list(csv.DictReader(ficheiro))

#Criar as linhas e importar os dados para a tabela 
linhas=""

for aluno in alunos:
    linhas+=f"""
        <tr>
            <td>{escape(aluno['Nome'])}</td>
            <td>{escape(aluno['Idade'])}</td>
            <td>{escape(aluno['Curso'])}</td>
            <td>{escape(aluno['Nota'])}</td>
        </tr>
    """
# Ler ficheiro html

html=ficheiro_html.read_text(encoding="UTF-8-sig")

inicio="<!-- INICIO -->"
fim="<!-- FIM -->"
if inicio not in html or fim not in html:
    raise ValueError("Marcadores não encontrados")
antes,resto=html.split(inicio,1) 
_, depois=resto.split(fim,1)

html=antes+inicio+linhas+fim+depois

#Guardar o ficheiro no HTML

ficheiro_html.write_text(html,encoding="UTF-8-sig")

print("Tabela atual atualizada com sucesso!")