import os
import shutil

print("===Organizador de ficheiros===")

pasta = input("Digite o caminho que deseja organizar: ")

categorias = {
    "Imagens" : [".jpg", ".jpeg", ".png", ".gif"],
    "Documentos": [".pdf", ".doc", ".txt"],
    "Audio": ["mp3","wav"],
    "Vídeos": [".mp4","avi",".mov"],
    "Outros": []
}

for categoria in categorias:
    caminho_subpasta = os.path.join(pasta, categoria)
    if not os.path.isfile(caminho_subpasta):
        os.mkdir(caminho_subpasta)

for fichero in os.listdir(pasta):
    caminho_ficheiro = os.path.join(pasta, fichero)
    if os.path.isfile(caminho_ficheiro):
        nome, extensao = os.path.splitext(fichero)

        movido = False
        for categoria, extensions in categorias.items():
            if extensao.lower() in extensions:
                shutil.move(caminho_ficheiro, os.path.join(pasta, categoria, fichero))
                movido = True
                break
        if not movido:
            shutil.move(caminho_ficheiro, os.path.join(pasta,"Outros", fichero))

print("Organização concluida")
