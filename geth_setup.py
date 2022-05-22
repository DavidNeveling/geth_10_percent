import os, shutil
geth_url = 'https://gethstore.blob.core.windows.net/builds/geth-linux-amd64-1.10.17-25c9b49f.tar.gz'
geth_file_name = str(geth_url[geth_url.rfind('/') + 1:])
os.system('wget ' + str(geth_url))
os.system('tar -xvf ' + geth_file_name)
shutil.copy('./' + geth_file_name + '/geth', '.')
shutil.rmtree(geth_file_name)