import Register_File as rf 
import Helper as hp
import Memory as mem

def add(instruction, PC):
    reg1 = instruction[7: 10]
    reg2 = instruction[10: 13]
    reg3 = instruction[13: 16]
 
    rf.setRegInt(reg2, 15)
    rf.setRegInt(reg3,15) #Use this kind of functions to set registers to some value and check your function

    a = hp.convertReg2int(rf.getReg(reg2))
    b = hp.convertReg2int(rf.getReg(reg3))
    
    ans  = a + b
    ansBin = hp.convertBinary(ans)
   
    if len(ansBin) > 16:
        rf.setOverflow(1)
        rf.setRegString(reg1, ansBin[len(ansBin) - 16:])
        
    else:
        rf.setRegString(reg1, hp.convertBinary16(ans))
    
    return PC + 1



def subtraction(instruction, PC):
	reg1 = instruction[7:10]
	reg2 = instruction[10:13]
	reg3 = instruction[13:16]

	#rf.setRegInt(reg2, 2)
	#rf.setRegInt(reg3,3)

	operand1 = hp.convertReg2int(rf.getReg(reg2))
	operand2 = hp.convertReg2int(rf.getReg(reg3))
	result = operand1 - operand2

	if(result < 0):
		result = 0
		rf.setOverflow(1)

	rf.setRegString(reg1, hp.convertBinary16(result))
	
	
	return (PC + 1)

def move_immediate(instruction, PC):
	reg1 = instruction[5:8]
	imm = instruction[8:]
	
	imm_value_in_int = hp.convertString2int(imm)
	
	bin_rep = hp.convertBinary16(imm_value_in_int)
	
	rf.setRegString(reg1, bin_rep)

	return (PC + 1)

def move_register(instruction, PC):
	reg1 = instruction[10:13]
	reg2 = instruction[13:]

	reg_value = rf.getReg(reg2)
	rf.setRegString(reg1, reg_value)

	return (PC + 1)

def multiply(instruction, PC):
    reg1 = instruction[7: 10]
    reg2 = instruction[10: 13]
    reg3 = instruction[13: 16]
 
    rf.setRegInt(reg2, 15)
    rf.setRegInt(reg3,15) #Use this kind of functions to set registers to some value and check your function

    a = hp.convertReg2int(rf.getReg(reg2))
    b = hp.convertReg2int(rf.getReg(reg3))
    
    ans  = a * b
    ansBin = hp.convertBinary(ans)
   
    if len(ansBin) > 16:
        rf.setOverflow(1)
        rf.setRegString(reg1, ansBin[len(ansBin) - 16:])
        
    else:
        rf.setRegString(reg1, hp.convertBinary16(ans))
    
    return PC + 1

def divide(instruction, PC):
	reg1 = instruction[10:13]
	reg2 = instruction[13:]
	
	rf.setRegInt(reg, 15)
	rf.setRegInt(reg2,15) #Use this kind of functions to set registers to some value and check your function
	a = hp.convertReg2int(rf.getReg(reg))
	b = hp.convertReg2int(rf.getReg(reg2))
	ans  = a / b
	rem = a%b
	if(b == 0):
		print("divisor cant be 0")

	reg0 = "000"
	reg1 = "001"
	rf.setRegString(reg0, hp.convertBinary16(ans))
	rf.setRegString(reg1, hp.convertBinary16(rem))
		
	return PC + 1

def right_shift(instruction, PC):
	reg1 = instruction[5:8]
	imm = instruction[8:]
	#rf.setRegInt(reg1, 10)
	value_to_be_shifted = hp.convertReg2int(rf.getReg(reg1))
	imm_value_in_int = hp.convertString2int(imm)
	right_shifted = value_to_be_shifted >> imm_value_in_int

	bin_rep = hp.convertBinary16(right_shifted)
	rf.setRegString(reg1, bin_rep)

	return (PC + 1)


def left_shift(instruction, PC):
	reg1 = instruction[5:8]
	imm = instruction[8:]
	#rf.setRegInt(reg1, 5)
	value_to_be_shifted = hp.convertReg2int(rf.getReg(reg1))
	imm_value_in_int = hp.convertString2int(imm)
	left_shifted = value_to_be_shifted << imm_value_in_int

	bin_rep = hp.convertBinary16(left_shifted)
	rf.setRegString(reg1, bin_rep)

	return (PC + 1)

def Exclusive_or(instruction, PC):
	reg1 = instruction[7:10]
	reg2 = instruction[10:13]
	reg3 = instruction[13:16]

	#rf.setRegInt(reg2, 5)
	#rf.setRegInt(reg3,9)

	value1 = hp.convertReg2int(rf.getReg(reg2))
	value2 = hp.convertReg2int(rf.getReg(reg3))

	result = value1^value2
	bin_rep = hp.convertBinary16(result)

	rf.setRegString(reg1, bin_rep)

	return (PC + 1)


def bitwise_or(instruction, PC):
	reg1 = instruction[7:10]
	reg2 = instruction[10:13]
	reg3 = instruction[13:16]

	#rf.setRegInt(reg2, 5)
	#rf.setRegInt(reg3,9)

	operand1 = rf.getReg(reg2)
	operand2 = rf.getReg(reg3)

	result = []

	for i in range(len(operand1)):
		result.append(int(int(operand1[i]) or int(operand2[i])))

	rf.setRegList(reg1, result)

	return (PC + 1)


def bitwise_and(instruction, PC):
	reg1 = instruction[7:10]
	reg2 = instruction[10:13]
	reg3 = instruction[13:16]

	#rf.setRegInt(reg2, 5)
	#rf.setRegInt(reg3,9)

	operand1 = rf.getReg(reg2)
	operand2 = rf.getReg(reg3)

	result = []

	for i in range(len(operand1)):
		result.append(int(int(operand1[i]) and int(operand2[i])))

	rf.setRegList(reg1, result)

	return (PC + 1)

def invert(instruction, PC):
	reg1 = instruction[10:13]
	reg2 = instruction[13:]

	#rf.setRegInt(reg2, 5)
	#rf.setRegInt(reg3,9)

	value1 = hp.convertReg2int(rf.getReg(reg2))

	result = ~value1
	bin_rep = hp.convertBinary16(result)

	rf.setRegString(reg1, bin_rep)

	return (PC + 1)

def compare(instruction, PC):
	reg1 = instruction[10:13]
	reg2 = instruction[13:]

	#rf.setRegInt(reg2, 5)
	#rf.setRegInt(reg3,9)

	value1 = hp.convertReg2int(rf.getReg(reg1))
	value2 = hp.convertReg2int(rf.getReg(reg2))

	if value1 == value2:
		rf.setEqual(1)
	elif value1 > value2:
		rf.setGreater(1)
	else:
		rf.setLower(1)
	
	return (PC + 1)


def halt(instruction, PC):
    print(hp.convertBinary8(PC) + " "*8)
    for register in rf.Register_Table.values():
        print(hp.convertIntList2String(register) + " "*8)
    mem.dumpMemory()
    exit()