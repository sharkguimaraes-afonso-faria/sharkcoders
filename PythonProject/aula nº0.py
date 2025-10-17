# Jogo da advihação em Phyton
import random

#Mensagem inicial
print("Jogo da Adivinhação")
print("Estou a pensar num número entre 1 e 10...")

numero_secreto = random.randint(1, 10)

palpite = int (input ("Qual número você acha que é? "))

if palpite == numero_secreto:
    print("Acertou! yeahhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")
elif palpite > numero_secreto:
    print("Muito alto! O número secreto foi maior que o palpite")
else:
    print("Muito baixo!! O número secreto foi menor que o palpite")
