import helper as hp
import Opcode_Table as op
R0 = [0]*16
R1 = [0]*16
R2 = [0]*16
R3 = [0]*16
R4 = [0]*16
R5 = [0]*16
R6 = [0]*16
FLAGS = [0]*16
PC = -1
MEM = "this is memory"

def input():
    pass

def main():
    global PC
    while True:
        PC += 1
        instruction = input()
        opcode = hp.getDigits(instruction,0,5)
        op.callOpcode(opcode)
    

