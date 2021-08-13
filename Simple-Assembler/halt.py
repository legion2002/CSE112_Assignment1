import error as er

def halt_error(instructions_file):
    flag = 0
    for instruction in instructions_file.values():
        
        if flag == 1 and len(instruction)!= 0:
            print(er.error_file["i"])
            exit()

        if len(instruction) == 1 and instruction[0] == "hlt":
            flag = 1
            
        elif len(instruction) >= 1 and instruction[0] == "hlt":
            print(er.error_file["k"])
            exit()
        
    if flag == 0:
        print(er.error_file["h"])
    exit()


# dic =  {1: ['var', 'x'], 2: ['var', 'y'], 3: ['add', 'a', 'b', 'c'], 4: ['label_check:'], 5: [], 6: ['add', 'x', 'y', 'z'], 7: [], 8: ['hlt'], 9: ['hlt']}
# halt_error(dic)