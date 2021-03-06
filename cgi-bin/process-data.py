import os
import pandas as pd 
import matplotlib.pyplot as plt
import json

json_folder = '../json/'
img_folder = '../img/'
acertos_folder = '../listas/acertos/'
basename = []
nameHtmlFile = []
lista6 = []
lista7 = []
lista9 = []
htmlNav = ["<nav>\n", "<nav>\n", "<nav>\n"]
html = ["", "", ""]
html_header = """<!DOCTYPE html>
    <html lang="pt-br">

    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="/css/acertos.css">
    <title>Lista de Matemática</title>
    </head>

    <body>\n"""

for files in os.listdir(json_folder):
    basename.append(files)

basename.sort()
print(basename)

html[0] = html_header
html[1] = html_header
html[2] = html_header
nameHtmlFile.append(os.path.join(acertos_folder, '6.html'))
nameHtmlFile.append(os.path.join(acertos_folder, '7.html'))
nameHtmlFile.append(os.path.join(acertos_folder, '9.html'))

i = 0
for filename in basename:
    base = os.path.splitext(filename)[0]
    with open(os.path.join(json_folder, filename)) as file:
        dataJson = json.load(file)

    data = pd.DataFrame.from_dict(dataJson, orient='index')
    lista = data['Lista'][0]
    serie = data['Serie'][0]
    del data['Lista']
    del data['Serie']
    data = data.sort_values('Acertos', ascending=False)

    
    nameFigFile = os.path.join(img_folder, base) + '.png'

    print(filename)
    if(serie == '9'):
        j = 2
        lista9.append(lista)
    elif(serie == '7'):
        j = 1
        lista7.append(lista)
    else:
        j = 0
        lista6.append(lista)
    html[j] += """<h1 id="{0}">Lista de Matemática - {1}: Acertos</h1>\n""".format(lista, lista)
    html[j] += data.to_html()

    acerto = {'Acertos': [0, 0, 0, 0, 0]}
    for value in data['Acertos']:
        if(value == 0):
            acerto['Acertos'][0] += 1
        elif(value == 1):
            acerto['Acertos'][1] += 1
        elif(value == 2):
            acerto['Acertos'][2] += 1
        elif(value == 3):
            acerto['Acertos'][3] += 1
        else:
            acerto['Acertos'][4] += 1

    df = pd.DataFrame(acerto,columns=['Acertos'],index = ['0 acertos','1 acerto','2 acertos','3 acertos','4 acertos'])
    #  df.plot.pie(subplots=True, figsize=(12, 12),autopct='%1.1f%%', startangle=0)
    #  plt.title('Gráfico de Acertos')
    
    #  plt.savefig(nameFigFile)

    #  html[j] += """\n<img src="{0}" alt="graph" height="100%" width="100%">\n""".format('../' + nameFigFile)
    i += 1

for id in lista6:
    htmlNav[0] += """<a href="#{0}">Lista {1}</a>\n""".format(id, id)
htmlNav[0] += "</nav>\n"

for id in lista7:
    htmlNav[1] += """<a href="#{0}">Lista {1}</a>\n""".format(id, id)
htmlNav[1] += "</nav>\n"

for id in lista9:
    htmlNav[2] += """<a href="#{0}">Lista {1}</a>\n""".format(id, id)
htmlNav[2] += "</nav>\n"


for k in range(len(html)):
    html[k] += "\n</body>\n" + htmlNav[k] + "</html>\n"
    with open(nameHtmlFile[k], 'w') as f:
        f.write(html[k])
    
