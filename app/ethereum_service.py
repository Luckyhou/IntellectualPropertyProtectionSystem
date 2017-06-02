from time import sleep
import json
from web3 import Web3, KeepAliveRPCProvider, contract
from binascii import unhexlify
import functools


class EthereumException(Exception):
    pass


web3 = Web3(KeepAliveRPCProvider(host='localhost', port='8545'))
eth = web3.eth
web3.personal.unlockAccount(eth.accounts[0], '4869', 0)

contract_data = {
    'abi': json.loads('[{"constant":true,"inputs":[{"name":"hash","type":"bytes32"}],"name":"getProofOwner","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"testException","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"hash","type":"bytes32"}],"name":"getPrice","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"hash","type":"bytes32"},{"name":"name","type":"string"},{"name":"description","type":"string"},{"name":"price","type":"uint256"}],"name":"proof","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"","type":"bytes32"}],"name":"proofs","outputs":[{"name":"name","type":"string"},{"name":"description","type":"string"},{"name":"timestamp","type":"uint256"},{"name":"owner","type":"address"},{"name":"forSell","type":"bool"},{"name":"price","type":"uint256"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"hash","type":"bytes32"}],"name":"isExisting","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"hash","type":"bytes32"},{"name":"user","type":"address"}],"name":"authorize","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"hash","type":"bytes32"},{"name":"name","type":"string"},{"name":"description","type":"string"},{"name":"forSell","type":"bool"},{"name":"price","type":"uint256"},{"name":"owner","type":"address"}],"name":"proof","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"hash","type":"bytes32"}],"name":"getProofDescription","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"hash","type":"bytes32"},{"name":"name","type":"string"},{"name":"description","type":"string"},{"name":"owner","type":"address"}],"name":"proof","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"hash","type":"bytes32"},{"name":"user","type":"address"}],"name":"transfer","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"hash","type":"bytes32"},{"name":"name","type":"string"},{"name":"description","type":"string"},{"name":"price","type":"uint256"},{"name":"owner","type":"address"}],"name":"proof","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"a","type":"int256"},{"name":"b","type":"int256"}],"name":"add","outputs":[{"name":"","type":"int256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"hash","type":"bytes32"},{"name":"name","type":"string"},{"name":"description","type":"string"}],"name":"proof","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"hash","type":"bytes32"}],"name":"purchase","outputs":[],"payable":true,"type":"function"},{"constant":true,"inputs":[{"name":"hash","type":"bytes32"}],"name":"isForSell","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"hash","type":"bytes32"},{"name":"user","type":"address"}],"name":"purchase","outputs":[],"payable":true,"type":"function"},{"constant":true,"inputs":[{"name":"hash","type":"bytes32"}],"name":"getProofName","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"test","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"hash","type":"bytes32"}],"name":"getProofTimestamp","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"}]'),
    'code': '6060604052341561000c57fe5b5b6118ef8061001c6000396000f30060606040523615610110576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff1680631fc2a3361461011257806325ffb6361461017657806331d98b3f146101885780634156e327146101c0578063444d95b0146102735780634628b41c146104025780634d89084b1461043e57806353d33bd9146104815780637213e7061461055e578063732b9fbd1461060957806379ce9fac146106d25780638f447dcb14610715578063a5f3c23b146107e7578063b03225ea14610824578063cc445611146108ce578063d019c139146108ea578063e56422a214610926578063eceddd4d14610961578063f8a8fd6d14610a0c578063fb49802d14610a1e575bfe5b341561011a57fe5b610134600480803560001916906020019091905050610a56565b604051808273ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200191505060405180910390f35b341561017e57fe5b610186610a9f565b005b341561019057fe5b6101aa600480803560001916906020019091905050610aa7565b6040518082815260200191505060405180910390f35b34156101c857fe5b61027160048080356000191690602001909190803590602001908201803590602001908080601f0160208091040260200160405190810160405280939291908181526020018383808284378201915050505050509190803590602001908201803590602001908080601f01602080910402602001604051908101604052809392919081815260200183838082843782019150505050505091908035906020019091905050610ad0565b005b341561027b57fe5b610295600480803560001916906020019091905050610ae7565b6040518080602001806020018781526020018673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020018515151515815260200184815260200183810383528981815460018160011615610100020316600290048152602001915080546001816001161561010002031660029004801561036a5780601f1061033f5761010080835404028352916020019161036a565b820191906000526020600020905b81548152906001019060200180831161034d57829003601f168201915b50508381038252888181546001816001161561010002031660029004815260200191508054600181600116156101000203166002900480156103ed5780601f106103c2576101008083540402835291602001916103ed565b820191906000526020600020905b8154815290600101906020018083116103d057829003601f168201915b50509850505050505050505060405180910390f35b341561040a57fe5b610424600480803560001916906020019091905050610b4e565b604051808215151515815260200191505060405180910390f35b341561044657fe5b61047f60048080356000191690602001909190803573ffffffffffffffffffffffffffffffffffffffff16906020019091905050610b64565b005b341561048957fe5b61055c60048080356000191690602001909190803590602001908201803590602001908080601f0160208091040260200160405190810160405280939291908181526020018383808284378201915050505050509190803590602001908201803590602001908080601f01602080910402602001604051908101604052809392919081815260200183838082843782019150505050505091908035151590602001909190803590602001909190803573ffffffffffffffffffffffffffffffffffffffff16906020019091905050610d53565b005b341561056657fe5b610580600480803560001916906020019091905050610fa0565b60405180806020018281038252838181518152602001915080519060200190808383600083146105cf575b8051825260208311156105cf576020820191506020810190506020830392506105ab565b505050905090810190601f1680156105fb5780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b341561061157fe5b6106d060048080356000191690602001909190803590602001908201803590602001908080601f0160208091040260200160405190810160405280939291908181526020018383808284378201915050505050509190803590602001908201803590602001908080601f0160208091040260200160405190810160405280939291908181526020018383808284378201915050505050509190803573ffffffffffffffffffffffffffffffffffffffff16906020019091905050611067565b005b34156106da57fe5b61071360048080356000191690602001909190803573ffffffffffffffffffffffffffffffffffffffff1690602001909190505061107e565b005b341561071d57fe5b6107e560048080356000191690602001909190803590602001908201803590602001908080601f0160208091040260200160405190810160405280939291908181526020018383808284378201915050505050509190803590602001908201803590602001908080601f0160208091040260200160405190810160405280939291908181526020018383808284378201915050505050509190803590602001909190803573ffffffffffffffffffffffffffffffffffffffff16906020019091905050611225565b005b34156107ef57fe5b61080e600480803590602001909190803590602001909190505061123c565b6040518082815260200191505060405180910390f35b341561082c57fe5b6108cc60048080356000191690602001909190803590602001908201803590602001908080601f0160208091040260200160405190810160405280939291908181526020018383808284378201915050505050509190803590602001908201803590602001908080601f0160208091040260200160405190810160405280939291908181526020018383808284378201915050505050509190505061124a565b005b6108e8600480803560001916906020019091905050611261565b005b34156108f257fe5b61090c600480803560001916906020019091905050611270565b604051808215151515815260200191505060405180910390f35b61095f60048080356000191690602001909190803573ffffffffffffffffffffffffffffffffffffffff169060200190919050506112a6565b005b341561096957fe5b61098360048080356000191690602001909190505061155d565b60405180806020018281038252838181518152602001915080519060200190808383600083146109d2575b8051825260208311156109d2576020820191506020810190506020830392506109ae565b505050905090810190601f1680156109fe5780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b3415610a1457fe5b610a1c611624565b005b3415610a2657fe5b610a40600480803560001916906020019091905050611656565b6040518082815260200191505060405180910390f35b600060006000836000191660001916815260200190815260200160002060030160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1690505b919050565b60006000fd5b565b60006000600083600019166000191681526020019081526020016000206004015490505b919050565b610ae08484846001856000610d53565b5b50505050565b6000602052806000526040600020600091509050806000019080600101908060020154908060030160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff16908060030160149054906101000a900460ff16908060040154905086565b60006000610b5b83611656565b1190505b919050565b600060006000610b7385610a56565b92503373ffffffffffffffffffffffffffffffffffffffff168373ffffffffffffffffffffffffffffffffffffffff16141580610bdb57508373ffffffffffffffffffffffffffffffffffffffff168373ffffffffffffffffffffffffffffffffffffffff16145b15610be65760006000fd5b6000600086600019166000191681526020019081526020016000206006019150600090505b8180549050811015610ca2578373ffffffffffffffffffffffffffffffffffffffff168282815481101515610c3c57fe5b906000526020600020906002020160005b5060000160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff161415610c945760006000fd5b5b8080600101915050610c0b565b818054806001018281610cb5919061167f565b916000526020600020906002020160005b6040604051908101604052808773ffffffffffffffffffffffffffffffffffffffff16815260200142815250909190915060008201518160000160006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff160217905550602082015181600101555050505b5050505050565b6000610d5e87610b4e565b151515610d6b5760006000fd5b856000600089600019166000191681526020019081526020016000206000019080519060200190610d9d9291906116b1565b50846000600089600019166000191681526020019081526020016000206001019080519060200190610dd09291906116b1565b50426000600089600019166000191681526020019081526020016000206002018190555081905060008173ffffffffffffffffffffffffffffffffffffffff161415610e1a573390505b8060006000896000191660001916815260200190815260200160002060030160006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff1602179055508360006000896000191660001916815260200190815260200160002060030160146101000a81548160ff02191690831515021790555082600060008960001916600019168152602001908152602001600020600401819055506000600088600019166000191681526020019081526020016000206007018054806001018281610f009190611731565b916000526020600020906002020160005b6040604051908101604052808573ffffffffffffffffffffffffffffffffffffffff16815260200142815250909190915060008201518160000160006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff160217905550602082015181600101555050505b50505050505050565b610fa8611763565b6000600083600019166000191681526020019081526020016000206001018054600181600116156101000203166002900480601f01602080910402602001604051908101604052809291908181526020018280546001816001161561010002031660029004801561105a5780601f1061102f5761010080835404028352916020019161105a565b820191906000526020600020905b81548152906001019060200180831161103d57829003601f168201915b505050505090505b919050565b6110778484846000600086610d53565b5b50505050565b600061108983610a56565b90503373ffffffffffffffffffffffffffffffffffffffff168173ffffffffffffffffffffffffffffffffffffffff161415806110f157508173ffffffffffffffffffffffffffffffffffffffff168173ffffffffffffffffffffffffffffffffffffffff16145b156110fc5760006000fd5b600060008460001916600019168152602001908152602001600020600701805480600101828161112c9190611731565b916000526020600020906002020160005b6040604051908101604052808573ffffffffffffffffffffffffffffffffffffffff16815260200142815250909190915060008201518160000160006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff160217905550602082015181600101555050508160006000856000191660001916815260200190815260200160002060030160006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff1602179055505b505050565b61123485858560018686610d53565b5b5050505050565b600081830190505b92915050565b61125b838383600060006000610d53565b5b505050565b61126c8160006112a6565b5b50565b600060006000836000191660001916815260200190815260200160002060030160149054906101000a900460ff1690505b919050565b60006000600060006112b786611270565b15156112c35760006000fd5b84935060008473ffffffffffffffffffffffffffffffffffffffff1614156112e9573393505b8373ffffffffffffffffffffffffffffffffffffffff1661130987610a56565b73ffffffffffffffffffffffffffffffffffffffff16141561132b5760006000fd5b6000600087600019166000191681526020019081526020016000206005019250600091505b82805490508210156113e7578373ffffffffffffffffffffffffffffffffffffffff16838381548110151561138157fe5b906000526020600020906003020160005b5060000160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1614156113d95760006000fd5b5b8180600101925050611350565b6113f086610aa7565b9050348111156114005760006000fd5b60006000876000191660001916815260200190815260200160002060050180548060010182816114309190611777565b916000526020600020906003020160005b6060604051908101604052808873ffffffffffffffffffffffffffffffffffffffff16815260200185815260200142815250909190915060008201518160000160006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff160217905550602082015181600101556040820151816002015550505060006000876000191660001916815260200190815260200160002060030160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff166108fc829081150290604051809050600060405180830381858888f19350505050151561155457fe5b5b505050505050565b611565611763565b6000600083600019166000191681526020019081526020016000206000018054600181600116156101000203166002900480601f0160208091040260200160405190810160405280929190818152602001828054600181600116156101000203166002900480156116175780601f106115ec57610100808354040283529160200191611617565b820191906000526020600020905b8154815290600101906020018083116115fa57829003601f168201915b505050505090505b919050565b60003373ffffffffffffffffffffffffffffffffffffffff161415151561164b5760006000fd5b60016001819055505b565b60006000600083600019166000191681526020019081526020016000206002015490505b919050565b8154818355818115116116ac576002028160020283600052602060002091820191016116ab91906117a9565b5b505050565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f106116f257805160ff1916838001178555611720565b82800160010185558215611720579182015b8281111561171f578251825591602001919060010190611704565b5b50905061172d91906117f8565b5090565b81548183558181151161175e5760020281600202836000526020600020918201910161175d919061181d565b5b505050565b602060405190810160405280600081525090565b8154818355818115116117a4576003028160030283600052602060002091820191016117a3919061186c565b5b505050565b6117f591905b808211156117f15760006000820160006101000a81549073ffffffffffffffffffffffffffffffffffffffff02191690556001820160009055506002016117af565b5090565b90565b61181a91905b808211156118165760008160009055506001016117fe565b5090565b90565b61186991905b808211156118655760006000820160006101000a81549073ffffffffffffffffffffffffffffffffffffffff0219169055600182016000905550600201611823565b5090565b90565b6118c091905b808211156118bc5760006000820160006101000a81549073ffffffffffffffffffffffffffffffffffffffff02191690556001820160009055600282016000905550600301611872565b5090565b905600a165627a7a72305820086cfcce74d604ccdf7e48b8293ec15b0e56814d2b630f086e4840cfd086725d0029',
    # 'code_runtime': '0x...',
    # 'source': 'contract Token {.....}',
}

# MyContract = contract.Contract.factory(web3, contract_name='MyContract', abi=contract_data['abi'], bytecode=contract_data['code'])
MyContract = contract.Contract.factory(web3, contract_name='MyContract', abi=contract_data['abi'])


def get_block(block_num):
    return eth.getBlock(block_num)


def get_transaction(tx):
    return eth.getTransaction(tx)


def get_latest_block():
    return eth.getBlock('latest')


def get_latest_block_number():
    return get_latest_block()['number']


def get_block_by_tx(tx):
    transaction = get_transaction(tx)
    return None if transaction is None else get_block(transaction['blockNumber'])


def get_tx_distance(tx):
    tx = get_transaction(tx)
    if tx['blockNumber'] is None:
        return None
    else:
        return get_latest_block_number() - tx['blockNumber']


def submit_file(file):
    address = "0x0ce6000fe53550ff2927bead4278be63357cbf7f"
    my_contract = contract.Contract.factory(web3, contract_name='MyContract', abi=contract_data['abi'], address=address)
    price = web3.toWei(file.price, "ether")
    file_hash = bytearray(unhexlify(file.hash))
    owner = "0x0000000000000000000000000000000000000000"

    gas_limit = web3.eth.getBlock('latest')['gasLimit']
    gas_estimate = my_contract.estimateGas().proof(file_hash, file.filename, file.description, file.for_sell, price, owner)

    if gas_estimate > gas_limit * 9 / 10:
        raise EthereumException

    return my_contract.transact().proof(file_hash, file.filename, file.description, file.for_sell, price, owner)


def traversal_all_contract():
    for i in range(0, eth.blockNumber + 1):
        if eth.getBlockTransactionCount(i) > 0:
            block = eth.getBlock(i)
            for transaction in block['transactions']:
                contractAddress = eth.getTransactionReceipt(transaction)['contractAddress']
                print(i, block['hash'], transaction, contractAddress)


def deploy_contract():
    return MyContract.deploy()


def load_contract(address):
    print('contract:', address)
    # contract_factory = contract.construct_contract_factory(web3, contract_data['abi'])
    # my_contract = contract_factory(address=address)
    my_contract = contract.Contract.factory(web3, contract_name='MyContract', abi=contract_data['abi'], address=address)
    result = my_contract.call().add(1, 2)
    print('add result:', result)

    print('proof timestamp:', my_contract.call().getProofName("aaaaa"))

    gas_limit = int(eth.getBlock('latest')['gasLimit'])
    # tx = my_contract.transact().proof("aaa", "bb", "cc")
    tx = my_contract.transact({'gas': int(gas_limit*0.9)}).proof("aaaaa", "bbb", "cc")
    print(tx)

    while True:
        receipt = eth.getTransactionReceipt(tx)
        if receipt is not None:
            break
        sleep(1)
    print('receipt:', receipt)

    from datetime import datetime

    now = datetime.now()
    print(now)
    new_data = str(now)
    print('try to set new data:', new_data)
    tx_list = []
    for i in range(1):
        tx = my_contract.transact().setData(new_data)
        # tx = my_contract.transact({'gas': 210000}).setData(new_data)
        tx_list.append(tx)
        print('tx hash:', tx)
    while len(tx_list) > 0:
        for tx in tx_list:
            receipt = eth.getTransactionReceipt(tx)
            if receipt is not None:
                tx_list.remove(tx)
                # print('tx receive:', receipt)
                print('tx %s receipt: blockNumber: %s, transactionIndex: %s' % (tx, receipt['blockNumber'], receipt['transactionIndex']))
        data = my_contract.call().getData()
        print('contract data:', data)

        if len(tx_list) > 0:
            sleep(2)
    print(datetime.now())


def test_deploy():
    tx_hash = deploy_contract()
    print('tx_hash:', tx_hash)
    while True:
        receipt = eth.getTransactionReceipt(tx_hash)
        if receipt is not None:
            break
        sleep(2)
    print('receipt:', receipt)
    print('contract:', receipt['contractAddress'])


if __name__ == '__main__':
    print('blockNum', eth.blockNumber)

    # unlock
    print('unlock', web3.personal.unlockAccount(eth.coinbase, '4869'), 0)

    # traversal_all_contract()

    # test_deploy()

    # load_contract("0x0b02516fdb53cd5f06547d5dda0b0bfe8d0ba1c6")
    load_contract("0x76ab884bbe0252f490a557c4117b6c6d1ce533af")