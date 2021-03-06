type_opcode = {
    "add":['A',"00000"],"sub":['A',"00001"],"mov1":['B',"00010"],"mov2":['C',"00011"],"ld":['D',"00100"],"st":['D',"00101"],
    "mul":['A',"00110"],"div":['C',"00111"],"rs":['B',"01000"],"ls":['B',"01001"],"xor":['A',"01010"],"or":['A',"01011"],"and":['A',"01100"],
    "not":['C',"01101"],"cmp":['C',"01110"],"jmp":['E',"01111"],"jlt":['E',"10000"],"jgt":['E',"10001"],"je":['E',"10010"],"hlt":['F',"10011"],
    "mov":['G', "11111"]
}

type_dict = {
    'A' : ["opcode", "u", "u", "reg", "reg", "reg"],
    'B' : ["opcode", "reg", "imm"],
    'C' : ["opcode", "u", "u", "u", "u", "u", "reg", "reg"],
    'D' : ["opcode", "reg", "mem"],
    'E' : ["opcode", "u", "u", "u", "mem"],
    'F' : ["opcode", "u", "u", "u", "u", "u", "u", "u", "u", "u", "u", "u" ]
}
type_length = {
    'A' : 4,
    'B' : 3,
    'C' : 3,
    'D' : 3,
    'E' : 2,
    'F' : 1

}

registers = {
    "R0": "000" , "R1": "001" , "R2": "010" , "R3": "011", "R4": "100" , "R5": "101" , "R6": "110" , "FLAGS": "111"
}
