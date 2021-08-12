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
            if(line != ''):
                processing(line, count)
            
            count += 1
        except EOFError:
            break


def converter():
    
    for address in instructions_file.keys:
        instruction = instructions_file[address]
        converted = ""
        if(instruction[-1] == ":"):
            st.processLabel(instruction[0],address)
        else:
            onverted = op.processInst(instruction[0], address)
            


#main execution starts here
def main():
    #first pass across text
    # createSymbol(inst)
    inp() #pass1
    print(instructions_file)
    st.createSymbol(instructions_file) #pass2
    print(st.Variables)
    print(st.Label)
   # convertBinary #pass3

    


main()

