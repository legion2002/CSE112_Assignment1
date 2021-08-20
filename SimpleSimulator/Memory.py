import Helper as hp

MEM = [[0]*16]*256

def setMemoryBin(address : str, value : str):
    #takes binary string address and binary string value and sets memory accordingly
    assert len(address) == 8, "Invalid memory address"
    assert len(value) == 16, "Invalid memory value"
    addressInt = int(address,2)
    MEM[addressInt] = hp.convertString2IntList(value)

def getMemoryBin(address : str):
    #gets using binary string address and returns value of memory as string
    assert len(address) == 8, "Invalid memory address"
    addressInt = int(address, 2)
    return hp.convertIntList2String(MEM[addressInt])

def getMemoryInt(address : int):
    #gets using integer address
    assert 0 <= address < 256, "Invalid memory address"
    return hp.convertIntList2String(MEM[address])

def setMemoryInt(address : int, value : str):
   
    assert address < 256, "Invalid memory address"
    
    MEM[address] = hp.convertString2IntList(value)
    

def dumpMemory():
    for row in MEM:
        print(hp.convertIntList2String(row))


