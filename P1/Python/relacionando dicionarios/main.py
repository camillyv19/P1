pacientes = {
    1001: {"nome": "cami", "idade": 19, "telefone": 99999999},
}
medico = {
    2001: {"nome": "joao", "idade": 41, "telefone": 88888888, "especialidade": "cardiologista"},
}
agendamento = {
    3001: {"paciente": "cami", "medico": "joao", "data": 14, "hora": 10},
}
usuario = (input("-----MENU-----\n(1)Adicionar médico\n(2)Adicionar paciente\n(3)Realizar agendamento\nEscolha uma opção: "))
if usuario == 1:
  add_medico = input("Digite o nome, idade, telefone e especialidade do médico")
  medico.append(add_medico)



print(usuario)
print(pacientes)
print(medico)
print(agendamento)