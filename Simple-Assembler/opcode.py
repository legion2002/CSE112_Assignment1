def processOpcode(instr,address):
    for key in type_opcode.keys():
        if( key == instr):
            return type_opcode["key"]
    TypoError(address)

def processInst(instr,address):
    binary = ''
    opReturn = processOpcode(instr,address)
    type = opReturn[0]
    opcode = opReturn[1]
    base = type_dict[type]
    for item in base:
        if item == 'opcode':
            binary += opcode
        elif item == 'u':
            binary += '0'
        elif item == 'imm':
            #somebody make this
            processImm()
        elif item == 'reg':
            #somebody make this
            processReg()
        elif item == 'mem':
            #somebody make this
            processMem()
        else:
            GeneralError()
        return binary
    

type_opcode = {
    "add":['A',"00000"],"sub":['A',"00001"],"mov1":['B',"00010"],"mov2":['C',"00011"],"ld":['D',"00100"],"st":['D',"00101"],
    "Mul":['A',"00110"],"div":['C',"00111"],"rs":['B',"01000"],"ls":['B',"01001"],"xor":['A',"01010"],"or":['A',"01011"],"and":['A',"01100"],
    "not":['C',"01101"],"cmp":['C',"01110"],"jmp":['E',"01111"],"jlt":['E',"10000"],"jgt":['E',"10001"],"je":['E',"10010"],"hlt":['F',"10011"]
}

type_dict = {
    'A' : ["opcode", "u", "u", "reg", "reg"],
    'B' : ["opcode", "reg", "imm"],
    'C' : ["opcode", "u", "u", "u", "u", "u", "reg", "reg"],
    'D' : ["opcode", "reg", "mem"],
    'E' : ["opcode", "u", "u", "u", "mem"],
    'F' : ["opcode", "u", "u", "u", "u", "u", "u", "u", "u", "u", "u", "u" ]
}

registers = {
    "r0": "000" , "r1": "001" , "r2": "010" , "r3": "011", "r4": "100" , "r5": "101" , "r6": "110" , "FLAGS": "111"
}
