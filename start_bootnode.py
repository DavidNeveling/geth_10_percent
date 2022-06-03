import os, subprocess, gen_genesis, time, threading, signal, sys

# def signal_handler(sig, frame):
#     sys.exit(0)

def launch_server():
    os.system('python3 -m http.server')

def launch_node(datadir, vhost, restrict_list):
    os.system('geth --datadir ' + datadir + ' --networkid 1231234512 --nat extip:`curl ipinfo.io/ip` --http.api web3,eth,debug,personal,net,admin,miner --http --http.addr "0.0.0.0" --http.port 8080 --http.corsdomain "*" --ipcdisable --port 30304 --verbosity 4 --http.vhosts "'+ vhost +'" --netrestrict ' + restrict_list + ' --mine --allow-insecure-unlock 2>/var/log/gethConsole.log 2>/var/log/gethConsole.log')


# signal.signal(signal.SIGINT, signal_handler)

datadir = './test/data'
vhost = '192-53-166-228.ip.linodeusercontent.com'
restrict_list = '"20.246.80.0/24","216.227.194.0/24","20.246.82.0/24","192.53.166.0/24","20.246.12.0/24"'
if not os.path.exists(datadir):
    os.makedirs(datadir)
password = 'a'
tmpfile = 'tmp'
file = open(tmpfile, 'w')
password_string = password + '\n' + password + '\n'
file.write(password_string)
file.close()
while not os.path.exists(tmpfile):
    time.sleep(0.1)
output = subprocess.run('./geth account new --datadir ' + datadir + ' < ' + tmpfile, capture_output=True, shell=True)
stdout = output.stdout.decode('ascii')
stdout = stdout[stdout.find('Public address'):]
stdout = stdout[:stdout.find('\n')]
account_address = stdout[stdout.find(' ') + 1:]
gen_genesis.create_genesis_file(account_address)
os.system('geth init --datadir ' + datadir + ' genesis.json')
x = threading.Thread(target=launch_server, args=())
y = threading.Thread(target=launch_node, args=(datadir, vhost, restrict_list))
x.start()
y.start()
y.join()
x.join()