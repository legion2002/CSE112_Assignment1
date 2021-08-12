import Symbol_Table as st
import opcode as op
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
            if(instruction[-1] == ":"):
                st.processLabel(instruction[0],address)
            else:
                converted = op.processInst(instruction[0], address)
            


#main execution starts here
def main():
    
    inp() #pass1
    st.createSymbol(instructions_file)
    converter()
   # BigErrors() #checks generic errors in the whole file like halt
    #converter() #converts code line by line and checks for line-by-line error
    



    


main()

