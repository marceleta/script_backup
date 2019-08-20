import sys, os
from datetime import date
import zipfile

DIAS = [
    'segunda',
    'terca',
    'quarta',
    'quinta',
    'sexta',
    'sabado',
    'domingo'
]

hoje = date.today()
cmd = sys.argv[:]
nome = cmd[1]
tipo_zip = cmd[2]
fonte = cmd[3]
destino = cmd[4]

if cmd[1] == 'help':
    print('exemplo:python3 backup.py nome diretorio/arquivo c:\\path\fonte\\ c:\\path\\destino\\ \n')

else:
    print('backup')
    nome = destino + '\\' +nome+ '_'+DIAS[hoje.weekday()]+ '.zip'
    backup_zip = zipfile.ZipFile(nome, 'w',zipfile.ZIP_DEFLATED) 


    if tipo_zip == 'arquivo':
       backup_zip.write(fonte)

    elif tipo_zip == 'diretorio':
        for root, dirs, files in os.walk(fonte):
            for f in files:
                backup_zip.write(os.path.join(root, f))

    backup_zip.close()


