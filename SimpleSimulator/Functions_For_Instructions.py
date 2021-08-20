import Register_File as rf 
import Helper as hp
import Memory as mem
import matplotlib.pyplot as plt

def add(instruction, PC):
    reg1 = instruction[7: 10]
    reg2 = instruction[10: 13]
    reg3 = instruction[13: 16]
    
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

	operand1 = hp.convertReg2int(rf.getReg(reg2))
	operand2 = hp.convertReg2int(rf.getReg(reg3))
	result = operand1 - operand2

	if(result < 0):
		result = 0
		rf.setOverflow(1)

	rf.setRegString(reg1, hp.convertBinary16(result))
	
	return PC + 1


def move_immediate(instruction, PC):
	reg1 = instruction[5:8]
	imm = instruction[8:]
	
	imm_value_in_int = hp.convertString2int(imm)
	bin_rep = hp.convertBinary16(imm_value_in_int)
	rf.setRegString(reg1, bin_rep)

	return PC + 1


def move_register(instruction, PC):
	reg1 = instruction[10:13]
	reg2 = instruction[13:]

	reg_value = rf.getReg(reg2)
	rf.setRegString(reg1, reg_value)
	rf.setRegList("111",[0]*16)

	return PC + 1


def load(instruction, PC, cycle):
	reg = instruction[5:8]
	memory = instruction[8:]

	plt.scatter(cycle, hp.convertString2int(memory), c = "blue")
	mem_value = mem.getMemoryBin(memory)
	value = hp.convertString2int(mem_value)
	rf.setRegInt(reg, value)

	return PC + 1


def store(instruction, PC, cycle):
	reg = instruction[5:8]
	mem_add = instruction[8:]
	plt.scatter(cycle, hp.convertString2int(mem_add), c = "blue")
	# rf.setRegInt(reg, 12)
	reg_val = rf.getReg(reg)
	bin_rep_reg = hp.convertIntList2String(reg_val)
	mem.setMemoryBin(mem_add, bin_rep_reg)

	return PC + 1


def multiply(instruction, PC):
    reg1 = instruction[7: 10]
    reg2 = instruction[10: 13]
    reg3 = instruction[13: 16]
 
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
	reg = instruction[10:13]
	reg2 = instruction[13:]
	
	a = hp.convertReg2int(rf.getReg(reg))
	b = hp.convertReg2int(rf.getReg(reg2))
	if(b == 0):
		print("divisor cant be 0")
	ans  = int(a / b)
	rem = int(a%b)

	reg0 = "000"
	reg1 = "001"
	rf.setRegString(reg0, hp.convertBinary16(ans))
	rf.setRegString(reg1, hp.convertBinary16(rem))
		
	return PC + 1


def right_shift(instruction, PC):
	reg1 = instruction[5:8]
	imm = instruction[8:]

	value_to_be_shifted = hp.convertReg2int(rf.getReg(reg1))
	imm_value_in_int = hp.convertString2int(imm)
	right_shifted = value_to_be_shifted >> imm_value_in_int

	bin_rep = hp.convertBinary16(right_shifted)
	rf.setRegString(reg1, bin_rep)

	return PC + 1


def left_shift(instruction, PC):
	reg1 = instruction[5:8]
	imm = instruction[8:]

	value_to_be_shifted = hp.convertReg2int(rf.getReg(reg1))
	imm_value_in_int = hp.convertString2int(imm)
	left_shifted = value_to_be_shifted << imm_value_in_int

	bin_rep = hp.convertBinary16(left_shifted)
	rf.setRegString(reg1, bin_rep)

	return PC + 1


def Exclusive_or(instruction, PC):
	reg1 = instruction[7:10]
	reg2 = instruction[10:13]
	reg3 = instruction[13:16]

	value1 = hp.convertReg2int(rf.getReg(reg2))
	value2 = hp.convertReg2int(rf.getReg(reg3))

	result = value1^value2
	bin_rep = hp.convertBinary16(result)

	rf.setRegString(reg1, bin_rep)

	return PC + 1


def bitwise_or(instruction, PC):
	reg1 = instruction[7:10]
	reg2 = instruction[10:13]
	reg3 = instruction[13:16]

	operand1 = rf.getReg(reg2)
	operand2 = rf.getReg(reg3)

	result = []
	for i in range(len(operand1)):
		result.append(int(int(operand1[i]) or int(operand2[i])))

	rf.setRegList(reg1, result)

	return PC + 1


def bitwise_and(instruction, PC):
	reg1 = instruction[7:10]
	reg2 = instruction[10:13]
	reg3 = instruction[13:16]

	operand1 = rf.getReg(reg2)
	operand2 = rf.getReg(reg3)

	result = []
	for i in range(len(operand1)):
		result.append(int(int(operand1[i]) and int(operand2[i])))

	rf.setRegList(reg1, result)

	return PC + 1


def invert(instruction, PC):
	reg1 = instruction[10:13]
	reg2 = instruction[13:]

	value1 = hp.convertReg2int(rf.getReg(reg2))
	result = ~value1 & (pow(2,16)-1)
	bin_rep = hp.convertBinary16(result)
	rf.setRegString(reg1, bin_rep)

	return PC + 1


def compare(instruction, PC):
	reg1 = instruction[10:13]
	reg2 = instruction[13:]

	value1 = hp.convertReg2int(rf.getReg(reg1))
	value2 = hp.convertReg2int(rf.getReg(reg2))

	if value1 == value2:
		rf.setEqual(1)
	elif value1 > value2:
		rf.setGreater(1)
	else:
		rf.setLower(1)
	
	return PC + 1


def unconditional_jump(instruction, PC):
	mem_add = instruction[8:]
	PC = hp.convertString2int(mem_add)

	return PC


def small_jump(instructions,PC):
	memory = instructions[8:]
	mem_add = hp.convertString2int(memory)
	smaller_than_flag = rf.getReg("111")[13]

	if smaller_than_flag == 1:
		PC = mem_add
	else:
		PC = PC + 1
		
	rf.setRegList("111",[0]*16)

	return PC


def greater_jump(instructions,PC):
	memory = instructions[8:]
	mem_add = hp.convertString2int(memory)
	greater_than_flag = rf.getReg("111")[14]

	if greater_than_flag == 1:
		PC = mem_add
	else:
		PC = PC +1

	rf.setRegList("111",[0]*16)

	return PC


def equal_jump(instruction, PC):
	mem_add = instruction[8:]
	mem_add_in_int = hp.convertString2int(mem_add)
	value_of_equal_flag = rf.getReg("111")[15]

	if(value_of_equal_flag == 1):
		PC = mem_add_in_int
	else:
		PC = PC + 1

	rf.setRegList("111",[0]*16)

	return PC


def halt(instruction, PC):

	print(hp.convertBinary8(PC), end = " ")
	for register in rf.Register_Table.values():
		print(hp.convertIntList2String(register), end =  " ")
	print()

	mem.dumpMemory()
	plt.savefig("Bonus_Question_Plot")
	exit()

