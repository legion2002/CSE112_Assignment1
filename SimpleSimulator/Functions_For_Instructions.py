import Register_File as rf 
import Helper as hp

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


def move_immediate(instruction, PC):
	reg1 = instruction[5:8]
	imm = instruction[8:]
	
	imm_value_in_int = hp.convertString2int(imm)
	
	bin_rep = hp.convertBinary16(imm_value_in_int)
	
	rf.setRegString(reg1, bin_rep)


def right_shift(instruction, PC):
	reg1 = instruction[5:8]
	imm = instruction[8:]
	#rf.setRegInt(reg1, 10)
	value_to_be_shifted = hp.convertReg2int(rf.getReg(reg1))
	imm_value_in_int = hp.convertString2int(imm)
	right_shifted = value_to_be_shifted >> imm_value_in_int

	bin_rep = hp.convertBinary16(right_shifted)
	rf.setRegString(reg1, bin_rep)


def left_shift(instruction, PC):
	reg1 = instruction[5:8]
	imm = instruction[8:]
	#rf.setRegInt(reg1, 5)
	value_to_be_shifted = hp.convertReg2int(rf.getReg(reg1))
	imm_value_in_int = hp.convertString2int(imm)
	left_shifted = value_to_be_shifted << imm_value_in_int

	bin_rep = hp.convertBinary16(left_shifted)
	rf.setRegString(reg1, bin_rep)









