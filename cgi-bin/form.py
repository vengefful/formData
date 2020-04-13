#!/usr/bin/env python
 
import cgi
import cgitb
import json
# from pushnotifier import PushNotifier as pn

""" pn = pn.PushNotifier('vengefful', 'lingua', 'Automation', 'D4DD52VB63CVV75B696VBV46696VV2VBTTFBKFBFBF')

def SendNotificationToIphoneX(data):
    fdata = f"{data['serie']} serie - lista {data['lista']} - {data['name']}\nRespondeu a atividade"
    pn.send_text(fdata, silent=False, devices=['Q1W5']) """

cgitb.enable()

#  print("Content-Type: text/plain\n\n") # HTTP header to say HTML is following
print ("Content-type:text/html\r\n\r\n")
print ('<html>')
print ('<head>')
#  print ('<title>Hello World - First CGI Program</title>')
print ('</head>')
print ('<body>')
#  print ('<h2>Hello World! This is my first CGI program</h2>')
print('<font size="7">')

formData = cgi.FieldStorage()
jsonData = formData.getvalue("foo")
data = json.loads(jsonData)
acertos = 0

for key in data:
    aluno = key

lista = data[aluno]['Lista']
filenameGab = '../listas/gabaritos/' + data[aluno]['Serie'] + '.json'
filename = '../json/' + data[aluno]['Serie'] + lista + 'Tests.json' 

with open(filenameGab) as file:
    gabarito = json.load(file)

for k in range(4):
    if(data[aluno]['Q' + str(k+1)] == gabarito[lista]['Q' + str(k+1)]):
        acertos += 1
    else:
        pass
data[aluno]['Acertos'] = acertos

try:
    with open(filename) as file:
        test = json.load(file)
        if aluno in test.keys():
            print('<p>Pode enviar apenas uma resposta</p>')
        else:
            tmpData = {'name': aluno, 'serie': data[aluno]['Serie'], 'lista': data[aluno]['Lista']}
            SendNotificationToIphoneX(tmpData)
            data.update(test)
            with open(filename, 'w') as file:
                json.dump(data, file, indent=2)
            print("Resposta enviada com sucesso")
except IOError:
    with open(filename, 'w') as file:
        json.dump(data, file, indent=2)
    print("Resposta enviada com sucesso!")
except Exception as e:
    pass
    print("Erro enviando resultados, por favor, reenvie!")

print('</font>')
print ('</body>')
print ('</html>')
#  try:
    #  with open("Testes.json", 'a+') as file:
        #  json.dump(data, file, indent=2)
    #  print("Resposta enviada")
#  except Exception as e:
    #  print(e)
