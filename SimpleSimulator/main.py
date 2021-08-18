import Helper as hp
import Register_File as rf
import Memory as mem
import Processing as ps
import matplotlib.pyplot as plt
PC = 0
cycle = 0

def inp():
    count = 0
    while True:
        try:
            
            line = input().strip()
            
            
            
            mem.setMemoryInt(count, line)
            
            count += 1
        except EOFError:
            break
    
        
def output(PC):
    # print("hello")
        
    print(hp.convertBinary8(PC) , end = " ")
    for register in rf.Register_Table.values():
        print(hp.convertIntList2String(register) , end = " ")
    print()
    

def refresh(instruction):
    opcode = instruction[0:5]
    if opcode == "10001" or opcode == "10000" or opcode == '10010' :
        return
    elif opcode == "00011" and instruction[13:16] == "111":
        return
    else:
        rf.setRegList("111", [0]*16)



def SetPlot():
    plt.xlabel("Cycles")
    plt.ylabel("Memory Address Accessed")
    plt.title("Bonus Question")

def BonusPlot(instruction, cycle):
    plt.scatter(cycle, instruction, c = "blue")
    

def main():
    inp()
    global PC
    global cycle
    SetPlot()
    while True:
        oldPC = PC
        cycle += 1
        instruction = mem.getMemoryInt(PC)
        BonusPlot(PC, cycle)
        
        refresh(instruction)
        PC = ps.process(instruction, PC)
        output(oldPC)
        #output was here originally
        
        
main()

