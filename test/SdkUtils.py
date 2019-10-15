import json
from punica.invoke.invoke_contract import Invoke
from punica.test.test import Test
from ontology.utils.util import parse_neo_vm_contract_return_type_integer, parse_neo_vm_contract_return_type_string, parse_neo_vm_contract_return_type_bool
from ontology.ont_sdk import OntologySdk

sdkInstance = None
wallet_path= 'wallet/wallet.json'

def GetDefaultNetwork():
    with open('./tests/TestsConfig.json') as file:  
        data = json.load(file)
        defaultNetwork = data["defaultNet"]
        return data["networks"][defaultNetwork]

def SendTransaction(contractAddress, acct, payer, abiFunction):    
    tx = GetSdk().neo_vm().send_transaction(
        contractAddress, 
        acct, 
        payer, 
        GetDefaultNetwork()["gasPrice"], 
        GetDefaultNetwork()["gasLimit"], 
        abiFunction, 
        False)
    return tx

def GetSdk():
    if sdkInstance == None:
        sdkInstance = OntologySdk()
        sdkInstance.set_rpc(GetDefaultNetwork()["networkUrl"])
        sdkInstance.wallet_manager.open_wallet(wallet_path)
    return sdkInstance

def GetDeployedContractAddress(contractName):
    with open('./contracts/Build/DeployedContracts.json') as file:  
        data = json.load(file)
        return data[contractName]
