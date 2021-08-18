import Helper as hp
import Register_File as rf
import Memory as mem
import Processing as ps

PC = 0

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
        
    print(hp.convertBinary8(PC) , end = " ")
    for register in rf.Register_Table.values():
        print(hp.convertIntList2String(register) , end = " ")
    print()

def refresh(instruction):
    opcode = instruction[0:5]
    if opcode == "10001" or opcode == "10000" or opcode == '10010' :
        return
    else:
        rf.setRegList("111", [0]*16)
        

def main():
    inp()
    global PC
    while True:
        
        instruction = mem.getMemoryInt(PC)
        refresh(instruction)
        PC = ps.process(instruction, PC)
        output(PC)
        
        
main()

