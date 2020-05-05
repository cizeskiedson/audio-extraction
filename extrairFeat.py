"""
@author: Gustavo Zanoni Felipe
@descprition: chamar o descritor acustico RP para todos os folds
@Date: 14/06/2017
"""

import os, shutil

#Pasta de origem dos audios
origem = '/home/edson/Documents/PIBIC/BaseFinal/'
saida = '/home/edson/Documents/PIBIC/BaseFinal/Autor/'
rp_extract = "/home/edson/Documents/PIBIC/python/projeto/rp_extract_batch.py"
classi = ['texto1', 'texto2', 'texto3', 'texto4', 'texto5']
genero = ['m', 'f']
idade = ['A', 'B', 'C', 'D']
folds = 1
contRP = 0
contRH = 0
contSSD = 0
lista = os.listdir(origem)
lista.sort()

for filename in lista:
    if not filename.endswith(".mp3"):
        continue
    else:
        #ex.: Processando audios... 
        print("Processando audios...  " + filename + "\n")
        dir_in = origem
        #ex.: fold1-beach
        out_file = filename
        dir_out = saida
        #python rp_extract_batch.py <input_path> <feature_file_name>
        rp = "python " + rp_extract + " " + dir_in + " " + out_file

        #os.chdir(dir_in)
        os.system(rp)

        if not os.path.exists(dir_out):
            os.makedirs(dir_out)
            print("Diretorio criado!")

        current = "/home/edson/env/ASC_PR-master/Baby_PR/AcousticStuff/rp_extract"
        for files in os.listdir(current):
            if files.endswith('.rp'):
                shutil.move(current + files, dir_out + files)
                contRP+= 1
                print("Arquivo RP movido: " +files + " #" + str(contRP))
            if files.endswith('.rh'):
                shutil.move(current + files, dir_out + files)
                contRH += 1
                print("Arquivo RH movido: " + files + " #" + str(contRH))
            if files.endswith('.ssd'):
                shutil.move(current + files, dir_out + files)
                contSSD += 1
                print("Arquivo SSD movido: " + files + " #" + str(contSSD))
            if files.endswith('.log'):
                shutil.move(current + files, dir_out + files)
print("Executado! Diretorios descritos: RP(" + str(contRP) + "), RH(" + str(contRH) + "), SSD(" + str(contSSD) + ")")