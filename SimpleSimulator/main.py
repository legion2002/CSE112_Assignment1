import Helper as hp
import Register_File as rf
import Memory as mem
import Processing as ps

PC = 0

def input():
    count = 0
    while True:
        try:
            line = input()
            
            mem.setMemoryInt(count, line)
            
            count += 1
        except EOFError:
            break
        
def output():
    print(hp.convertBinary8(PC) + " "*8)
    for register in rf.Register_Table.values():
        print(hp.convertIntList2String(register) + " "*8)

def main():
    input()
    global PC
    while True:
        instruction = mem.getMemoryInt(PC)
        ps.process(instruction, PC)
        
        
    

