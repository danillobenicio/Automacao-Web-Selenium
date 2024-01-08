import time
import os, sys, shutil
from datetime import date

#Constantes
loginlt = 'cpd@vancouros.com.br'
senhalt = ''
caminhoOrigem = r'C:/Users/danillo.VAN/Downloads/'
caminhoDestinoLT = r'//192.168.5.5/Dados/Usuario/Ti/Backups_semanais/LEATHER_NUVEM/'
caminhoDestinoGoDaddy = r'//192.168.5.5/Dados/Usuario/Ti/Backups_semanais/SITE_VANCOUROS/'
dataAtualPadraoSc = date.today().strftime('%m-%d-%Y')
dataAtualPadraoSc = dataAtualPadraoSc.lstrip('0').replace('-0', '-')
nomePasta = date.today().strftime('%Y-%m-%d');

def set_tempo(tempo):
    i = 1
    print("Espere " + str(tempo) + " segundos!")
    while i <= tempo:       
        print(i)
        time.sleep(1)
        i += 1


def verifica_diretorio(caminho, data):
    if os.path.isdir(caminho + data):
        print('Diretório já existe!')
    else:
        print('Criando diretório')
        os.mkdir(caminho + data)



