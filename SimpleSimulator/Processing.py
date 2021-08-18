import Functions_For_Instructions as f
import Register_File as rf
import Helper as hp
import Memory as mem

def process(instruction : str, PC):
    opcode = instruction[0:5]
    if opcode == "00000":
        return add(instruction, PC)
    elif opcode == "00001":
        return f.subtraction(instruction, PC)
    elif opcode == "00010":
        return f.move_immediate(instruction, PC)
    elif opcode == "00011":
        return f.move_register(instruction, PC)
    elif opcode == "00100":
        return f.load(instruction, PC)
    elif opcode == "00101":
        return f.store(instruction, PC)
    elif opcode == "00110":
        return f.multiply(instruction, PC)
    elif opcode == "00111":
        return f.divide(instruction, PC)
    elif opcode == "01000":
        return f.right_shift(instruction, PC)
    elif opcode == "01001":
        return f.left_shift(instruction, PC)
    elif opcode == "01010":
        return f.Exclusive_or(instruction, PC)
    elif opcode == "01011":
        return f.bitwise_or(instruction, PC)
    elif opcode == "01100":
        return f.bitwise_and(instruction, PC)
    elif opcode == "01101":
        return f.invert(instruction, PC)
    elif opcode == "01110":
        return f.compare(instruction, PC)
    elif opcode == "01111":
        return f.unconditional_jump(instruction, PC)
    elif opcode == "10000":
        return f.small_jump(instruction, PC)
    elif opcode == "10001":
        return f.greater_jump(instruction, PC)
    elif opcode == "10010":
        return f.equal_jump(instruction, PC)
    elif opcode == "10011":
        return halt(instruction, PC)

# start completing processing functions here, if your function doesn't update the program counter,
# add 1 to the program counter once you have processed your instruction
# basically it is the responsibility of your function to return the value of the correct program counter.

# add function is completed , refer to this
def add(instruction, PC):
    reg1 = instruction[7: 10]
    reg2 = instruction[10: 13]
    reg3 = instruction[13: 16]
    a = hp.convertReg2int(rf.getReg(reg2))
    b = hp.convertReg2int(rf.getReg(reg3))
    
    ans  = a + b
    ansBin = hp.convertBinary(ans)   
    if len(ansBin) > 16:
        rf.setOverflow(1)
        rf.setRegString(reg1, ansBin[len(ansBin) - 16:])
        
    else:
        rf.setRegString(reg1, hp.convertBinary16(ans))
    
    return PC + 1

def halt(instruction, PC):
    
    # print(hp.convertBinary8(PC), end = " ")
    # for register in rf.Register_Table.values():
    #     print(hp.convertIntList2String(register),end = " ")
    # print()
    mem.dumpMemory()
    exit()




    

# print(process("0000000001010011",5))




