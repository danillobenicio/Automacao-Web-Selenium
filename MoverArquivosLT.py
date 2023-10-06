import os, sys, shutil
from datetime import date
from funcoes import caminhoOrigem, caminhoDestinoLT, verifica_diretorio, dataAtual

verifica_diretorio(caminhoDestinoLT, dataAtual)

if os.path.exists(caminhoOrigem + 'backup-vancouros.myscriptcase.com-' + dataAtual + '.tar.gz'):
    print('Movendo arquivos')
    
    #Move
    shutil.move(caminhoOrigem + 'vancouro_sjv.sql.gz', caminhoDestinoLT + dataAtual)
    shutil.move(caminhoOrigem + 'vancouro_integracao.sql.gz', caminhoDestinoLT + dataAtual)
    shutil.move(caminhoOrigem + 'backup-vancouros.myscriptcase.com-' + dataAtual + '.tar.gz', caminhoDestinoLT + dataAtual)
else:
    print('Não há arquivos.')

print('Finalizado')