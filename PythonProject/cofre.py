
cofre = 0

meta = int(input("qual é o total que queres ter no cofre daqui a um tempinho???"))
while cofre < meta:
    deposito = int(input("quanto é queres depositar no cofre????"))
    if deposito > 0:
        cofre = cofre + deposito
        print("agora tens", cofre, "€ no cofre")

    else:
        print("depositação impossível")
print("atingiste a tua meta", meta,"€ foi atingida")