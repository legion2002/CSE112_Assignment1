


# print("hello this is tanishk")
instructions_file = {}
def processing(ins, count):
    ls = list(map(str,ins.strip().split()))
    instructions_file[count] = ls


    



def inp():
    count = 1

    for i in range(256):
        try:
            line = input()
            processing(line, count)
            count += 1
        except EOFError:
            break

        
       
            

def main():
    #first pass across text
    # createSymbol(inst)
    inp() #pass1
    createSymbol #pass2
    convertBinary #pass3

    createSymbol(instructions_file)
    for instruction in instructions_file:
        opcode_fetch(instruction[0],instruction.key)

inp()
print(instructions_file)
# a = input()
# print("This is what I have read" + a)
