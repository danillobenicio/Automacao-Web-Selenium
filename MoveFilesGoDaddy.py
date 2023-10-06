import os, sys, shutil
from datetime import date

#Current date
currentDate = date.today().strftime('%m-%d-%Y')

#Origin Path
originPath = r'C:/Users/danillo.VAN/Downloads/'

#Destinantion Path Go Daddy
destinationPathGoDaddy = r'//192.168.5.5/Dados/Usuario/Ti/Backups_semanais/SITE_VANCOUROS/'

if os.path.isdir(destinationPathGoDaddy + currentDate):
    print('Diretório já existe')
    print('Movendo arquivos')
else:
    print('Criando diretório')
    os.mkdir(destinationPathGoDaddy + currentDate)

#Check if files exist
if os.path.exists(originPath + 'backup-vancouros.com.br-' + currentDate + '.tar.gz'):
    #Move
    print('Movendo arquivos')
    shutil.move(originPath + 'vancouros.sql.gz', destinationPathGoDaddy + currentDate)
    shutil.move(originPath + 'backup-vancouros.com.br-' + currentDate + '.tar.gz', destinationPathGoDaddy + currentDate)
    shutil.move(originPath + 'db_contratos.sql.gz', destinationPathGoDaddy + currentDate)
else:
    print('There are no files')

print('Finished')