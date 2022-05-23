import json
# public_key = "0x4083F1fD75678836E69874B2E73974A675c7C10c"
def create_genesis_file(public_key):
    genesis_string = '{ "config": { "chainId": 1231234512, "homesteadBlock": 0, "eip150Block": 0, "eip155Block": 0, "eip158Block": 0, "byzantiumBlock": 0, "constantinopleBlock": 0, "petersburgBlock": 0, "clique": { "period": 5, "epoch": 30000 } }, "difficulty": "1", "gasLimit": "8000000", "extradata": "0x0000000000000000000000000000000000000000000000000000000000000000{0}0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000", "alloc": { "{0}": { "balance": "0xfffffffffffffffffffffffffffffff" } } }'#.format(public_key[public_key.find('x') + 1:])
    genesis_dict = json.loads(genesis_string)
    genesis_dict['extradata'] = genesis_dict['extradata'].format(public_key[public_key.find('x') + 1:])
    print(genesis_dict['alloc'].keys())
    genesis_dict['alloc'] = {list(genesis_dict['alloc'].keys())[0].format(public_key[public_key.find('x') + 1:]): list(genesis_dict['alloc'].values())[0]}
    genesis_string = json.dumps(genesis_dict)
    f = open('genesis.json', 'w')
    f.write(genesis_string)
