import shutil

origem = input("Escreva o caminho completo do ficheiro que quer mover")
destino = input("Escreva o nome da pasta de destino")

shutil.move(origem, destino)
print("Ficheiro movido com sucesso!")