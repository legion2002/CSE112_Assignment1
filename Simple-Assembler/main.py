import Symbol_Table as st
import opcode as op
import Errors_functions as er 
import processing as ps
#This dictionary contains instructions in the form {instruction_line_number : [list of strings]}
instructions_file = {}

# This function processes an input line
def processing(ins, count):
    ls = list(map(str,ins.strip().split()))
    instructions_file[count] = ls

#This function takes in the input till EOF
def inp():
    count = 1
    while True:
        try:
            line = input()
            
            processing(line, count)
            
            count += 1
        except EOFError:
            break


def converter():
    
    for address in instructions_file.keys():
        instruction = instructions_file[address]
        converted = ""
        if(instruction):
            if(instruction[0][-1] == ":"):
                converted = ps.processLabel(instruction,address)
            else:
                converted = ps.processInst(instruction,address)
            if(converted != "" and converted != None):
                print(converted) 


#main execution starts here
def main():
    
    inp() 
    
    st.createSymbol(instructions_file)
    er.BigErrors(instructions_file)
    converter()
  
    
    



    


main()

