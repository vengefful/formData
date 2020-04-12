//eslint-disable-next-line
function SaveToFile() {
  var numberTest = document.getElementById('test').innerText;
  var matchNumberTest = /\d{2}/g.exec(numberTest);
  var matchSerie = /\d{1}/g.exec(document.getElementById('serie').textContent);
  var answer = {};
  //var answersCorrect = {'Q1': 'B', 'Q2': 'A', 'Q3': 'A', 'Q4': 'E'};
  var AlunoAnswers = {};
  var nameAluno = document.getElementById("nameAluno").value;
  answer['Lista'] = matchNumberTest[0];
  //answer['Acertos'] = 0;
  answer['Serie'] = matchSerie[0];
  for (var i = 0; i < 4; i++) {
    var question = "questao0" + i.toString();
    var radios = document.getElementsByName(question);
    for (var j = 0, length = radios.length; j < length; j++) {
      if (radios[j].checked) {
        //if (radios[j].value == answersCorrect['Q' + (i + 1).toString()]) {
        //answer['Acertos'] += 1;
        //}
        answer['Q' + (i + 1).toString()] = radios[j].value;
      }
    }
  }
  AlunoAnswers[nameAluno] = answer;
  var json = JSON.stringify(AlunoAnswers);
  document.getElementById("foo").value = json;
}