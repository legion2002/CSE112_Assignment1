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
def changeArrayRegister( regCode : str, value):
    global R0
    global R1
    global R2
    global R3
    global R4
    global R5
    global R6
    global FLAGS
    assert len(value) == 16, "Something wrong with Register File Length"
    # assert type(value) is List, "Something wrong with Register File Type"
    if(regCode == '000'):
        R0 = value
        Register_Table[regCode] = R0
    elif (regCode == '001'):
        R1 = value
        Register_Table[regCode] = R1
    elif (regCode == '010'):
        R2 = value
        Register_Table[regCode] = R2
    elif (regCode == '011'):
        R3 = value
        Register_Table[regCode] = R3
    elif (regCode == '100'):
        R4 = value
        Register_Table[regCode] = R4
    elif (regCode == '101'):
        R5 = value
        Register_Table[regCode] = R5
    elif (regCode == '110'):
        R6 = value
        Register_Table[regCode] = R6
    elif (regCode == '111'):
        FLAGS = value
        Register_Table[regCode] = FLAGS
    else:
        print("There is some error in changeArrayRegister")


def getReg(regCode : str):
    assert regCode in Register_Table.keys(), "Registers Invalid"
    
    return Register_Table[regCode]

def setRegList(regCode : str, value):
    #value is an array of length 16
    
    assert regCode in Register_Table.keys(), "Registers Invalid"
    assert len(value) == 16, "Registers Invalid"
    changeArrayRegister(regCode, value)

def setRegString(regCode : str, value : str):
    #value is a string of length 16
    valueList = hp.convertString2IntList(value)
    assert regCode in Register_Table.keys(), "Registers Invalid"
    assert len(valueList) == 16, "Registers Invalid"
    changeArrayRegister(regCode, valueList)

def setRegInt(regCode : str, value : int):
    #value is an integer
    
    valueString = hp.convertBinary16(value)
    valueList = hp.convertString2IntList(valueString)
    assert regCode in Register_Table.keys(), "Registers Invalid"
    assert len(valueList) == 16, "Registers Invalid"
    changeArrayRegister(regCode, valueList)

def setOverflow(val : int):
    FLAGS[-4] = val
    Register_Table["111"] = FLAGS

def setGreater(val : int):
    FLAGS[-2] = val
    Register_Table['111'] = FLAGS

def setLower(val : int):
    FLAGS[-3] = val
    Register_Table["111"] = FLAGS

def setEqual(val : int):
    FLAGS[-1] = val
    Register_Table["111"] = FLAGS

def getOverflow():
    return FLAGS[-4]

def getGreater():
    return FLAGS[-2]

def getLower():
    return FLAGS[-3]

def getEqual():
    return FLAGS[-1]