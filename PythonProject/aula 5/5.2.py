def verificar_velocidades(velocidades,limite):
    for v in velocidades:
        if v > limite:
            print(v,"km/h -> acima do limite!")
        else:
            print(v,"km/h -> dentro do limite!")

velocidades_carros = [50, 70, 95, 190, 300]

limite_usuario = int(input("Qual é o limte da velocidade? "))
verificar_velocidades(velocidades_carros,limite_usuario)