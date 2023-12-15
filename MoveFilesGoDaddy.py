import os, sys, shutil
from datetime import date
from funcoes import dataAtualPadraoSc, caminhoOrigem, caminhoDestinoGoDaddy, verifica_diretorio, nomePasta

verifica_diretorio(caminhoDestinoGoDaddy, nomePasta)

if os.path.exists(caminhoOrigem + 'backup-vancouros.com.br-' + dataAtualPadraoSc + '.tar.gz'):
    print('Movendo arquivos, aguarde!')
    shutil.move(caminhoOrigem + 'vancouros.sql.gz', caminhoDestinoGoDaddy + nomePasta)
    shutil.move(caminhoOrigem + 'backup-vancouros.com.br-' + dataAtualPadraoSc + '.tar.gz', caminhoDestinoGoDaddy + nomePasta)
    shutil.move(caminhoOrigem + 'db_contratos.sql.gz', caminhoDestinoGoDaddy + nomePasta)
    shutil.move(caminhoOrigem + 'visitas_clientes.sql.gz', caminhoDestinoGoDaddy + nomePasta)
else:
    print('Não há arquivos')

print('Finalizado')