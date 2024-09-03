clientes = {
    1001: {'nome': 'Maria do Carmo', 'idade': 63, 'telefone': '83988885555'},
    1002: {'nome': 'Benedito', 'idade': 51, 'telefone': '83988885511'},
    1003: {'nome': 'Creusa', 'idade': 63, 'telefone': '83988886633'},
    1004: {'nome': 'Carlos Daniel', 'idade': 49, 'telefone': '83988889985'},
    1005: {'nome': 'Xerolayne', 'idade': 23, 'telefone': '83988881234'}
}

medicos = {
    'M001': {'nome': 'Macedo', 'idade': 41, 'telefone': '83984845151', 'especialidade': 'Proctologista'},
    'M002': {'nome': 'Marta', 'idade': 39, 'telefone': '83984845152', 'especialidade': 'Cardiologista'},
    'M003': {'nome': 'Melissa', 'idade': 32, 'telefone': '83984845153', 'especialidade': 'Ofdtalmologista'}
}

agenda = {
    'ag00001': {'paciente': 1001, 'medico': 'M002', 'data': '12/05/2024', 'hora': '17:00'},
    'ag00002': {'paciente': 1004, 'medico': 'M001', 'data': '13/05/2024', 'hora': '08:00'},
    'ag00003': {'paciente': 1005, 'medico': 'M003', 'data': '17/05/2024', 'hora': '12:00'},
}

print(clientes)
print(medicos)
print(agenda)