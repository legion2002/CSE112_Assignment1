import Symbol_Table as st
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

        
#main execution starts here
def main():
    #first pass across text
    # createSymbol(inst)
    inp() #pass1
    print(instructions_file)
    st.createSymbol(instructions_file) #pass2
    print(st.Variables)
   # convertBinary #pass3

    
    

main()

