import Errors_functions as er
# Label dictionary stores labels and its location in the format "abc" : 1
Label = {}

# Variables dictionary stores variables and its location in the format "x" : 2
Variables = {}

# To store location of the variables and labels 
program_counter = 0

def createSymbol(instructions_file):
	global program_counter
	for instruction in instructions_file.keys():
		if(not instructions_file[instruction]):
			continue
		if(len(instructions_file[instruction]) == 1):
			if(instructions_file[instruction][0] == "var"):
				er.GeneralError(instruction)
		
		if(len(instructions_file[instruction] )>2):
			if(instructions_file[instruction][0] == "var"):
				er.GeneralError(instruction)
				
		symbol = instructions_file[instruction][0]
		if(checkSymbol(symbol) == 1):
			# print(instructions_file[instruction])
			insertVariable(instructions_file[instruction][1], 0, instructions_file)
		elif(checkSymbol(symbol) == 2):
			insertLabel(symbol[:-1], program_counter, instructions_file)
			program_counter += 1
		else:
			program_counter += 1

	update_location_for_variables(Variables)


def update_location_for_variables(Variables):
	global program_counter
	for variable in Variables.keys():
		Variables[variable] = program_counter
		program_counter += 1


def insertLabel(label_name : str, label_location : int, instructions_file):
	global Label
	if(label_name not in Label):
		Label[label_name] = label_location
	else:
		for key, value in instructions_file.items():
			if(len(value) > 0 and (label_name + ":") == value[0]):
				line_num = key
		print("General Syntax Error" + " in line number :" + str(line_num))
		exit()




def insertVariable(variable_name : str, variable_location : int, instructions_file):
	global Variables
	if(variable_name not in Variables):
		Variables[variable_name] = variable_location
	else:
		for key, value in instructions_file.items():
			if(len(value) > 1 and (variable_name) == value[1] and value[0] == "var"):
				line_num = key
		print("General Syntax Error" + " in line number :" + str(line_num))
		exit()


def checkSymbol(symbol_name : str) -> int:
	if(symbol_name == 'var'):
		return 1
	elif(symbol_name[-1] == ':'):
		return 2
	else:
		return 3
