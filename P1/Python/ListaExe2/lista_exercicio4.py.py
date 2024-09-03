login_certo = "camilly"
senha_certa = "1234"
login = ""
senha = ""
while login != login_certo and senha != senha_certa:
    login = input("digite seu login: ")
    senha = input("digite sua senha: ")
    if login == login_certo and senha == senha_certa:
        print("você está logado! ")
    else:
        print("login ou senha inválido")
