#!/usr/bin/env python
 
import cgi
import cgitb
import requests
import json

cgitb.enable()

print("Content-Type: text/plain") # HTTP header to say HTML is following
#  print()

formData = cgi.FieldStorage()
jsonData = formData.getvalue("foo")
data = json.loads(jsonData)

for key in data:
    aluno = key

try:
    with open("Testes.json") as file:
        test = json.load(file)
        if aluno in test.keys():
            pass
            #  print("SAFADINHO, TA REPETINDO O TESTE NE SAFADO!!!! TE  PEGUEI MANE")
        else:
            data.update(test)
            with open("Testes.json", 'w') as file:
                json.dump(data, file, indent=2)
            #  print("Resposta enviada com sucesso")
except IOError:
    with open("Testes.json", 'w') as file:
        json.dump(data, file, indent=2)
    #  print("Resposta enviada com sucesso!")
except Exception as e:
    pass
    #  print("Erro enviando resultados, por favor, reenvie!")


#  try:
    #  with open("Testes.json", 'a+') as file:
        #  json.dump(data, file, indent=2)
    #  print("Resposta enviada")
#  except Exception as e:
    #  print(e)
