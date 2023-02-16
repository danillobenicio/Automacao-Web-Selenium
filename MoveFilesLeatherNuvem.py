import os, sys, shutil
from datetime import date

# Current Date
currentDate = date.today().strftime('%m-%d-%Y')

# Origin Path
originPath = r'C:/Users/danillo.VAN/Downloads/'

# Destinantion Path
destinationPath = r'//192.168.5.5/Dados/Usuario/Ti/Backups_semanais/LEATHER_NUVEM/'

# Check if directory exists
if os.path.isdir(destinationPath + currentDate):
    print('Directory already exists')
else:
    print('Creating directory')
    os.mkdir(destinationPath + currentDate)



# Check if files exist
if os.path.exists(originPath + 'backup-vancouros.myscriptcase.com-' + currentDate + '.tar.gz'):
    print('Moving files')
    
    #Move
    shutil.move(originPath + 'vancouro_sjv.sql.gz', destinationPath + currentDate)
    shutil.move(originPath + 'vancouro_integracao.sql.gz', destinationPath + currentDate)
    shutil.move(originPath + 'backup-vancouros.myscriptcase.com-' + currentDate + '.tar.gz', destinationPath + currentDate)
else:
    print('There are no files')

print('Finished')