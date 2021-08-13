def halt_error():
    counter = 0
    flag = 0
    for instruction in main.instructions_file:
        counter += 1
        if len(instruction)!= 1 and instruction[0] == "hlt":
            return "k"
        if len(instruction) == 1 and instruction[0] == "hlt":
            flag = 1
            if counter != len(main.instructions_file):
                return "i"
                
    if flag == 0:
        return "h"
    else:
        return 0
