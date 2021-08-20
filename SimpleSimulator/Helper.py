def convertBinary8(value):
    binRep = bin(value).replace("0b", "")
    while(len(binRep) < 8):
        binRep = "0" + binRep
    
    assert len(binRep) == 8, "something is wrong with the memory Value"
    return binRep


def convertBinary16(value):
    binRep = bin(value).replace("0b", "")
    while(len(binRep) < 16):
        binRep = "0" + binRep
    
    assert len(binRep) == 16, "something is wrong with the memory Value"
    return binRep


def convertBinary(value):
    return bin(value).replace("0b", "")


def convertIntList2String(listInteger):
    #returns the value of a list of integers to a string (Use to read register)
    return "".join(map(str,listInteger ))


def convertString2int(stringValue):
    #returns the value of the binary string to integer
    return int(stringValue,2)


def convertReg2int(regList):
    # returns the value of the register as an integer
    return int("".join(map(str,regList )),2)


def convertString2IntList(stringVal):
    return list(map(int, list(stringVal)))
 
    