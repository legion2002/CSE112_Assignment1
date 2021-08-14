import Symbol_Table as st
import error as er
import opcode as op



def misuseOfLabelsAndVariables():
	for variable_name in st.Variables:
		if(variable_name in st.Label):
			#check line num
			print(er.error_file["f"])
			exit()

	for label_name in st.Label:
		if(label_name in st.Variables):
			#check line num
			print(er.error_file["f"])
			exit()


def errorCheckImm(immediate_value : str, address : int):
	if(immediate_value[0] != "$"):
		print(er.error_file["k"] + " in line number : " + str(address))
		exit()
	imm_val = immediate_value[1:]
	if(imm_val.isnumeric()):
		if(not(int(imm_val) >= 0 and int(imm_val) <= 255)):
			print(er.error_file["e"] + " in line number : " + str(address))
			exit()
	else:
		print(er.error_file["e"] + " in line number : " + str(address))
		exit()


def TypoError(address : int):
	print(er.error_file["a"] + " in line number : " + str(address))
	exit()


def VariablesInBetween(instructions_file):
	flag = 0
	for instruction in instructions_file.values():
		if(instruction):
			if(instruction[0] != "var"):
				flag +=1 
			elif(instruction[0] == "var" and flag > 0):
				for key, value in instructions_file.items():
					if(value == instruction):
						line_number = key
						break
				print(er.error_file["g"] + " in line number :" + str(line_number))
				exit()


def GeneralError(address : int):
	print(er.error_file["k"] + " in line number :" + str(address))
	exit()


def WrongSyntax(address : int):
	print(er.error_file["j"] + " in line number :" + str(address))
	exit()


def errorCheckReg(reg_name : str, instruction, address : int):
	if(reg_name == "FLAGS" and instruction[0] != "mov"):

		print(er.error_file["d"] + " in line number : " + str(address))
		exit()
	
	if(reg_name == "FLAGS" and instruction[0] == "mov" and instruction[1] == "FLAGS"):
		print(er.error_file["d"] + " in line number : " + str(address))
		exit()

	if(reg_name not in op.registers.keys()):
		print(er.error_file["a"] + " in line number : " + str(address))
		exit()
		
	



def checkLabelAndVariableNames(instructions_file):
	for label_name in st.Label:
		if((label_name in op.type_opcode.keys() and label_name != "mov1" and label_name != "mov2") or label_name in op.registers.keys()):
			check_label = label_name + ":"
			for key, value in instructions_file.items():
				if(value[0] == check_label):
					line_number = key
					break
			print(er.error_file["k"] + " in line number :" + str(line_number))
			exit()

	for var_name in st.Variables:
		if((var_name in op.type_opcode.keys()and var_name != "mov1" and var_name != "mov2")or var_name in op.registers.keys() or var_name.isnumeric()):
			for key, value in instructions_file.items():
				if(value[0] == "var" and value[1] == var_name):
					address = key
					break
			print(er.error_file["k"]  + " in line number : " + str(address))
			exit()


def useOfUndefinedLabel(label_name : str, address : int):
	
	if(label_name not in st.Label):
		if(label_name in st.Variables):
			print(er.error_file["f"]  + " in line number : " + str(address))
			exit()
		else:
			print(er.error_file["c"]  + " in line number : " + str(address))
			exit()


def useOfUndefinedVariable(var_name : str, address : int):
	if(var_name not in st.Variables):
		if(var_name in st.Label):
			print(er.error_file["f"]  + " in line number : " + str(address))
			exit()
		else:
			print(er.error_file["b"]  + " in line number : " + str(address))
			exit()


def BigErrors(instructions_file):
	halt_error(instructions_file)
	VariablesInBetween(instructions_file)
	misuseOfLabelsAndVariables()
	
	checkLabelAndVariableNames(instructions_file)
	

def halt_error(instructions_file):
	flag = 0
	for instrComplete in instructions_file.items():
		instruction = instrComplete[1]
		address = instrComplete[0]
		if flag == 1 and len(instruction)!= 0:
			print(er.error_file["i"] + " in line number: " + str(address - 1))
			exit()

		if len(instruction) == 1 and instruction[0] == "hlt":
			flag = 1
            
		elif len(instruction) >= 1 and instruction[0] == "hlt":
			print(er.error_file["k"])
			exit()
		elif len(instruction) >= 1 and instruction[0][-1] == ":":
			if(len(instruction) == 2 and instruction[1] == "hlt"):
				flag = 1
			elif(len(instruction) > 2 and instruction[1] == "hlt"):
				print(er.error_file["k"])
				exit()

        
	if flag == 0:
		print(er.error_file["h"])
		exit()



#errorCheckReg("FLAGS", ["add", "FLAGS", "FLAGS", "r1"], 5)
