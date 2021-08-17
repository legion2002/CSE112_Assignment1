import Helper as hp

R0 = [0]*16
R1 = [0]*16
R2 = [0]*16
R3 = [0]*16
R4 = [0]*16
R5 = [0]*16
R6 = [0]*16
FLAGS = [0]*16

Register_Table  = {
    '000': R0,
    '001': R1,
    '010': R2,
    '011': R3,
    '100': R4,
    '101': R5,
    '110': R6,
    '111': FLAGS,
}
def getReg(regCode : str):
    assert regCode in Register_Table.keys(), "Registers Invalid"
    return Register_Table[regCode]

def setRegList(regCode : str, value):
    #value is an array of length 16
    assert regCode in Register_Table.keys(), "Registers Invalid"
    assert len(value) == 16, "Registers Invalid"
    Register_Table[regCode] = value

def setRegString(regCode : str, value : str):
    #value is a string of length 16
    valueList = list(value)
    assert regCode in Register_Table.keys(), "Registers Invalid"
    assert len(valueList) == 16, "Registers Invalid"
    Register_Table[regCode] = valueList

def setRegInt(regCode : str, value : int):
    #value is an integer
    valueList = hp.convertBinary16(value)
    assert regCode in Register_Table.keys(), "Registers Invalid"
    assert len(valueList) == 16, "Registers Invalid"
    Register_Table[regCode] = valueList

def setOverflow(val : int):
    FLAGS[-4] = val