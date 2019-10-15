import json
import os
import sys
from Compile import GetBuildFolderPath, GetAbiFilePath, GetContractsFolderPath

def Deploy(contractName):
    os.system("punica deploy --avm " + os.path.join(GetBuildFolderPath(), contractName) + ".avm --config " + os.path.join(GetContractsFolderPath(), contractName) + "-config.json")     
    
    with open(GetAbiFilePath(contractName), "r") as f:
        dict_abi = json.loads(f.read())
        contract_address_tmp = dict_abi['hash'].replace('0x', '')
        contract_address = [contract_address_tmp[i:i+2] for i in range(0, len(contract_address_tmp), 2)]
        
    return contract_address


if __name__ == '__main__':
    if (len(sys.argv) < 2):
        print("Contract name is required")
    else:
        contractName = sys.argv[1]
        address = Deploy(contractName)
        print("Deployed contract address: " + address)
