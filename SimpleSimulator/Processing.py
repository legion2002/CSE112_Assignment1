import Functions_For_Instructions as f
import Register_File as rf
import Helper as hp
import Memory as mem

def process(instruction : str, PC):
    opcode = instruction[0:5]
    if opcode == "00000":
        return f.add(instruction, PC)
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
    elif opcode == "01000":
        return f.compare(instruction, PC)
    elif opcode == "10011":
        return halt(instruction, PC)
    #Complete all elif with proper opcodes, as you keep making your functions


# start completing processing functions here, if your function doesn't update the program counter,
# add 1 to the program counter once you have processed your instruction
# basically it is the responsibility of your function to return the value of the correct program counter.

# add function is completed , refer to this

def halt(instruction, PC):
    print(hp.convertBinary8(PC) + " "*8)
    for register in rf.Register_Table.values():
        print(hp.convertIntList2String(register) + " "*8)
    mem.dumpMemory()
    exit()

# print(process("0000000001010011",5))




