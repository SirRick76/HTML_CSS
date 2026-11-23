import csv
import matplotlib.pyplot as plt 
from html import escape
from pathlib import Path

pasta=Path(__file__).resolve().parent
ficheiro_csv=pasta/"alunos.csv"
ficheiro_html=pasta/"matplotlib.html"

with open (ficheiro_csv,encoding="utf-8") as ficheiro:
     alunos=list(csv.DictReader(ficheiro))

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

nomes=[aluno["Nome"] for aluno in alunos]
notas=[int(aluno["Nota"]) for aluno in alunos]
idades=[int(aluno["Idade"]) for aluno in alunos]

plt.figure(figsize=(8,4))
plt.bar(nomes,notas,color="darkslategray")
plt.title("Notas dos Alunos")
plt.xlabel("Alunos")
plt.ylabel("Notas")
plt.ylim(0,20)
plt.savefig(pasta / "notas.png")
plt.close

#contar o numero de alunos para cada idade para criar o grafico

contagem={}
for idade in idades:
     contagem[idade]=contagem.get(idade,0)+1

idades_unicas=sorted(contagem)
quantidades=[contagem[idade] for idade in idades_unicas]

plt.figure(figsize=(8,4))
plt.bar([str(idade) for idade in idades_unicas], quantidades, color="darkslategray")
plt.title("Nº de alunos por idade")
plt.xlabel("Idade")
plt.ylabel("Número de alunos")
plt.yticks(range(0, max(quantidades,default=0)))
plt.tight_layout()
plt.savefig(pasta / "idades.png")
plt.close