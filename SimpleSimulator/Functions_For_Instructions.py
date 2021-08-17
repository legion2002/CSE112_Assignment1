import Register_File as rf 
import Helper as hp

def subtraction(instruction, PC):
	reg1 = instruction[7:10]
	reg2 = instruction[10:13]
	reg3 = instruction[13:16]

	rf.setRegInt(reg2, 7)
	rf.setRegInt(reg3,3)

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

	operand1 = getReg(reg2)
	operand2 = getReg(reg3)

	result = []

	for i in range(len(operand1)):
		result.append(int(int(operand1) or int(operand2)))

	rf.setRegList(reg1, result)

	return (PC + 1)

def bitwise_and(instruction, PC):
	reg1 = instruction[7:10]
	reg2 = instruction[10:13]
	reg3 = instruction[13:16]

	operand1 = getReg(reg2)
	operand2 = getReg(reg3)

	result = []

	for i in range(len(operand1)):
		result.append(int(int(operand1) and int(operand2)))

	rf.setRegList(reg1, result)







