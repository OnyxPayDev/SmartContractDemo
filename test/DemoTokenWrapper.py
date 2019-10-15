import json
from punica.invoke.invoke_contract import Invoke
from punica.test.test import Test
from ontology.utils.util import parse_neo_vm_contract_return_type_integer, parse_neo_vm_contract_return_type_string, parse_neo_vm_contract_return_type_bool
import SdkUtils

abiInfo = Test.get_abi_info('contracts/build/DemoToken_abi.json')
owner = "ATwo3VeAj4JnDY2uP1aKWS4p5LhyFHJeiE"
ownerAccount = SdkUtils.GetSdk().wallet_manager.get_account(owner, '123')

def ContractAddress():
    return bytes.fromhex(SdkUtils.GetDeployedContractAddress("DemoToken"))

def Init():
    params = dict()
    abiFunction = Invoke.get_function(params, 'init', abiInfo)
    return parse_neo_vm_contract_return_type_bool(SdkUtils.SendTransaction(ContractAddress(), owner, ownerAccount, abiFunction))

def Transfer(from_address, to_address, amount, payer):
    #transfer(from_address, to_address, amount)
    params = dict()
    params["from_address"] = from_address
    params["to_address"] = to_address
    params["amount"] = amount
    abiFunction = Invoke.get_function(params, 'transfer', abiInfo)
    return parse_neo_vm_contract_return_type_bool(SdkUtils.SendTransaction(ContractAddress(), from_address, payer, abiFunction))


def Balance(address):
    params = dict()
    params["address"] = address
    abiFunction = Invoke.get_function(params, 'balanceOf', abiInfo)
    return parse_neo_vm_contract_return_type_integer(SdkUtils.SendTransaction(ContractAddress(), owner, ownerAccount, abiFunction))
