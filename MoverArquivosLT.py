import os, sys, shutil
from datetime import date
from funcoes import caminhoOrigem, caminhoDestinoLT, verifica_diretorio, dataAtualPadraoSc, nomePasta

verifica_diretorio(caminhoDestinoLT, nomePasta)

if os.path.exists(caminhoOrigem + 'backup-vancouros.myscriptcase.com-' + dataAtualPadraoSc + '.tar.gz'):
    print('Movendo arquivos, aguarde!')
    shutil.move(caminhoOrigem + 'vancouro_sjv.sql.gz', caminhoDestinoLT + nomePasta)
    shutil.move(caminhoOrigem + 'vancouro_integracao.sql.gz', caminhoDestinoLT + nomePasta)
    shutil.move(caminhoOrigem + 'backup-vancouros.myscriptcase.com-' + dataAtualPadraoSc + '.tar.gz', caminhoDestinoLT + nomePasta)
else:
    print('Não há arquivos.')

print('Finalizado')