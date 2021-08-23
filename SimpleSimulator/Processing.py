import Functions_For_Instructions as f
import Register_File as rf
import Helper as hp


def process(instruction : str, PC, cycle):
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
        return f.load(instruction, PC, cycle)
    elif opcode == "00101":
        return f.store(instruction, PC, cycle)
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
        return f.halt(instruction, PC)

