import os
datadir = './test3/data'
remotevhost = '192-53-166-228.ip.linodeusercontent.com'
selfvhost = '192-53-166-228.ip.linodeusercontent.com'
os.system('wget -O genesis2.json ' + remotevhost + ':8000/genesis.json')
os.system('./geth init --datadir '+datadir+' genesis2.json')
os.system('./geth attach '+remotevhost+':8080 --exec admin.nodeInfo.enr > ENR') 
os.system('''./geth --datadir '''+datadir+''' --networkid 1231234512 --bootnodes `cat ENR | tr -d '"'` --http --http.port 8545 --http.corsdomain "*" --http.vhosts "'''+selfvhost+'''" --http.api web3,eth,debug,personal,net,admin --vmdebug --http.addr "0.0.0.0" --allow-insecure-unlock''')
