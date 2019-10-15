from ontology.compiler import Compiler
import os
import sys

rootPath = os.path.join(os.path.abspath(__file__), os.pardir)

def GetContractsFolderPath():
    return os.path.abspath(os.path.join(rootPath, "contracts"))

def GetBuildFolderPath():
    return os.path.abspath(os.path.join(GetContractsFolderPath(), "build"))

def GetTestFolderPath():
    return os.path.abspath(os.path.join(rootPath, "test"))


def GetContractFilePathWithoutextention(contractName):
    return os.path.abspath(os.path.join(GetContractsFolderPath(), contractName))


def GetAvmFilePath(contractName):
    return GetContractFilePathWithoutextention(contractName) + ".avm.str"


def GetAbiFilePath(contractName):
    return GetContractFilePathWithoutextention(contractName) + ".abi.json"


def GetDestAvmFilePath(contractName):
    return os.path.abspath(os.path.join(GetBuildFolderPath(), contractName) + ".avm")


def GetDestAbiFilePath(contractName):
    return os.path.abspath(os.path.join(GetBuildFolderPath(), contractName) + "_abi.json")


def GetAvmTmpFilePath(contractName):
    return GetContractFilePathWithoutextention(contractName) + ".avm"


def GetWarninFilePath(contractName):
    return GetContractFilePathWithoutextention(contractName) + ".warning"


def GetFunctionMapFilePath(contractName):
    return GetContractFilePathWithoutextention(contractName) + ".Func.Map"


def GetDebugJsonFilePath(contractName):
    return GetContractFilePathWithoutextention(contractName) + ".debug.json"


def RemoveIfExist(fileName):
    if os.path.exists(fileName):
        print("remove " + fileName)
        os.remove(fileName)

def MoveToBuild(fileName):
    RemoveIfExist(GetDestAvmFilePath(fileName))        
    destPath = GetDestAvmFilePath(fileName)
    os.rename(GetAvmFilePath(fileName), destPath)

    RemoveIfExist(GetDestAbiFilePath(fileName))        
    os.rename(GetAbiFilePath(fileName), GetDestAbiFilePath(fileName))
    return destPath


def RemoveArtifacts(contractName):
    os.remove(GetAvmTmpFilePath(contractName))
    os.remove(GetWarninFilePath(contractName))
    os.remove(GetFunctionMapFilePath(contractName))
    os.remove(GetDebugJsonFilePath(contractName))


def Compile(contractName):    
    sourceFile = os.path.join(GetContractsFolderPath(), contractName) + ".py"
    Compiler.Compile(sourceFile)
    destPath = MoveToBuild(contractName)
    RemoveArtifacts(contractName)
    return destPath


if __name__ == '__main__':
    if (len(sys.argv) < 2):
        print("Contract name is required")
    else:
        contractName = sys.argv[1]
        Compile(contractName)
        
