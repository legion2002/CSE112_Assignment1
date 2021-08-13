import Errors_functions as er
import opcode as op
import Symbol_Table as st

def processLabel(instruction,address):
    if(len(instruction) > 1):
        return processInst(instruction[1:], address)

def processOpcode(first,instruction,address):
    if(first == "mov"):
        if(len(instruction) != 3):
            er.GeneralError
        else:
            regCheck = instruction[2]
            for regName in op.registers.keys():

                if(regName == regCheck):
                    return op.type_opcode["mov2"]
            return op.type_opcode["mov1"]

            
    for key in op.type_opcode.keys():
        if( key == first):
            return op.type_opcode[key]
    er.TypoError(address)

def processInst(instr,address):
    
    #received complete instruction as instr
    binary = ''
    #getting opcode using instr[0]
    if instr[0] == "var":
        return binary
    else:
        opReturn = processOpcode(instr[0],instr,address)
        type = opReturn[0]
        #this is binary opcode
        opcode = opReturn[1]
        base = op.type_dict[type]
        if(op.type_length[type] != len(instr)):
            er.GeneralError(address)
        else:
            wordCount = 0
            for item in base:      

                if item == 'opcode':
                    # print(instr[wordCount])
                    binary += opcode
                elif item == 'u':
                    wordCount -= 1
                    binary += '0'
                elif item == 'imm':
                    # print(instr[wordCount])
                
                    binary += processImm(instr[wordCount],address)
                elif item == 'reg':
                    # print(instr[wordCount])
                    binary += processReg(instr[wordCount],instr,address)
                elif item == 'mem':
                
                    binary += processMem(instr[wordCount],instr,address)
                    
                    
                else:
                    er.GeneralError(address)
                    
                wordCount += 1
        return binary


    
def processImm(immString, address):
    er.errorCheckImm(immString, address)
    n = int(immString[1:])
    binRep = bin(n).replace("0b", "")
    while(len(binRep) < 8):
        binRep = "0" + binRep
    
    assert len(binRep) == 8, "something is wrong with the immediate Value"
    return binRep

def processReg(reg : str, instruction, address):

    # errorCheckReg(reg, instruction, address) --> this function checks for all FLAGS and register related errors
   
    er.errorCheckReg(reg, instruction, address) 
    for regName in op.registers.keys():

        if(regName == reg):
            return op.registers[regName]
        
    er.TypoError(address)

def processMem(mem, instruction, address):
    if(instruction[0] == "ld" or instruction[0] == "st"):
        er.useOfUndefinedVariable(mem, address)
        return convertBinary8(st.Variables[mem])
    else:
        er.useOfUndefinedLabel(mem,address)
        return convertBinary8(st.Label[mem])

def convertBinary8(value):
    
    binRep = bin(value).replace("0b", "")
    while(len(binRep) < 8):
        binRep = "0" + binRep
    
    assert len(binRep) == 8, "something is wrong with the memory Value"
    return binRep


