import os, subprocess, gen_genesis
datadir = '/opt/ethereum/data'
if os.path.exists(datadir):
    os.makedirs(datadir)
password = 'a'
tmpfile = 'tmp'
file = open(tmpfile, 'w')
password_string = password + '\n' + password + '\n'
file.write(password_string)
file.close()
output = subprocess.run('./geth account new --datadir ' + datadir + ' < ' + tmpfile, capture_output=True)
print(output)
# 1.1) snag the account/secret (without the 0x - like 87e4146428136a756be8e96aca006d87e459e457)
# 2) vi /opt/ethereum/genesis.json
# 2.1) add the genesis info for the extradata, alloc and the balance of 0xfffffffffffffffffffffffffffffff
# os.system('geth init --datadir /opt/ethereum/data /opt/ethereum/genesis.json')
# os.system('geth --datadir /opt/ethereum/data --networkid 1231234512 --nat extip:`curl ipinfo.io/ip` --http.api web3,eth,debug,personal,net,admin,miner --http --http.addr "0.0.0.0" --http.port 8080 --http.corsdomain "*" --ipcdisable --port 30304 --verbosity 4 --http.vhosts "50-116-24-194.ip.linodeusercontent.com" --netrestrict "20.246.80.0/24","216.227.194.0/24","20.246.82.0/24","192.53.166.0/24","20.246.12.0/24" --mine --allow-insecure-unlock 2>/var/log/gethConsole.log 2>/var/log/gethConsole.log')