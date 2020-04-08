#!/usr/bin/env python
 
import cgi
import cgitb
import requests
import json

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

for key in data:
    aluno = key

try:
    with open("../9ATestes.json") as file:
        test = json.load(file)
        if aluno in test.keys():
            print('<p>Não pode repetir o teste, seu professor estará de olho em você de agora por diante</p>')
        else:
            data.update(test)
            with open("../9ATestes.json", 'w') as file:
                json.dump(data, file, indent=2)
            print("Resposta enviada com sucesso")
except IOError:
    with open("../9ATestes.json", 'w') as file:
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
