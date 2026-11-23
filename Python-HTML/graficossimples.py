import csv
from html import escape
from pathlib import Path

pasta=Path(__file__).resolve().parent
ficheiro_csv=pasta/"alunos.csv"
ficheiro_html=pasta/"graficossimples.html"

with open (ficheiro_csv,encoding="utf-8") as ficheiro:
     alunos=list(csv.DictReader(ficheiro))

tabela=""
grafico_notas=""
contagem_idades={}

for aluno in alunos:
    nome = escape(aluno["Nome"])
    curso = escape(aluno["Curso"])
    idade = int(aluno["Idade"])
    nota = int(aluno["Nota"])

    tabela += f"<tr><td>{nome}</td><td>{idade}</td><td>{curso}</td><td>{nota}</td></tr>"
    # uma nota de 20 valores corresponde a 100% da barra
    largura = max(0,min(100,nota*5))
    grafico_notas+=f"""
        <div class="linha">
            <span class="nome">{nome}</span>
            <div class="fundo">
                <div class="barra" style="width:{largura}%"></div>
            </div>
            <span class="valor">{nota}</span>
        </div>\n
        """



html=ficheiro_html.read_text(encoding="UTF-8-sig")

inicio="<!-- INICIO -->"
fim="<!-- FIM -->"
if inicio not in html or fim not in html:
    raise ValueError("Marcadores não encontrados")
antes,resto=html.split(inicio,1) 
_, depois=resto.split(fim,1)

html=antes+inicio+tabela+fim+depois

#Guardar o ficheiro no HTML

ficheiro_html.write_text(html,encoding="UTF-8-sig")