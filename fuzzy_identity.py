import ethct
from web3 import Web3, HTTPProvider

web3 = Web3(HTTPProvider("https://ropsten.infura.io/v3/bda996b482e944bdbd5bad497e8f7205"))

from web3.auto import w3

flag = False

contract = ethct.Contract(abifile = "./build/returnAddress.abi", address = "0x2B237Cf8ed591fdc9709E943aCB34f84678c802a", provider_url = "http://localhost:8545")

while not flag:
    acc = w3.eth.account.create('')
    nonce = 0
    while nonce < 12:
        print('trying %s with nonce %d' % (acc.privateKey.hex(), nonce))
        arg_list = [acc.address, str(nonce)]
        contract_addr = contract.call('keccakHash', arg_list)
        if 'badc0de' in contract_addr.lower():
            print('privkey:', acc.privateKey)
            print('nonce:', nonce)
            flag = True
        nonce += 1
