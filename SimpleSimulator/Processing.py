import Register_File as rf
import Helper as hp
import Memory as mem

def process(instruction : str, PC):
    opcode = instruction[0:5]
    if opcode == "00000":
        return add(instruction, PC)
    elif opcode == "10011":
        return halt(instruction, PC)
    #Complete all elif with proper opcodes, as you keep making your functions


# start completing processing functions here, if your function doesn't update the program counter,
# add 1 to the program counter once you have processed your instruction
# basically it is the responsibility of your function to return the value of the correct program counter.

# add function is completed , refer to this
def add(instruction, PC):
    reg1 = instruction[7: 10]
    reg2 = instruction[10: 13]
    reg3 = instruction[13: 16]
    print(reg1, reg2, reg3)
    rf.setRegInt(reg2, 5)
    rf.setRegInt(reg3,6) #Use this kind of functions to set registers to some value and check your function
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
    print(hp.convertBinary8(PC) + " "*8)
    for register in rf.Register_Table.values():
        print(hp.convertIntList2String(register) + " "*8)
    mem.dumpMemory()
    exit()

print(process("0000000001010011",5))

    
