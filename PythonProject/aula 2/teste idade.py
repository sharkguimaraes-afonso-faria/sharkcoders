n_amigos = int(input("quantos amigos queres regisrar"))
for i in range(n_amigos):
    nome = input("digite seu nome: ")
    idade = int(input("digite sua idade: "))
    if idade > 18:
        print(nome, "é maior de idade")
    else:
        print(nome, "é menor de idade")