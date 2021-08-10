
# Label dictionary stores labels and its location in the format "abc" : 1
Label = {}

# Variables dictionary stores variables and its location in the format "x" : 2
Variables = {}

# To store location of the variables and labels 
program_counter = 0

def createSymbol(instructions_file):
	global program_counter
	for instruction in instructions_file.keys():
		symbol = instructions_file[instruction][0]
		if(checkSymbol(symbol) == 1):
			insertVariable(instructions_file[instruction][1], 0)
		elif(checkSymbol(symbol) == 2):
			insertLabel(symbol[:-1], program_counter)
			program_counter += 1
		else:
			program_counter += 1

	update_location_for_variables(Variables)


def update_location_for_variables(Variables):
	global program_counter
	for variable in Variables.keys():
		Variables[variable] = program_counter
		program_counter += 1


def insertLabel(label_name : str, label_location : int):
	global Label
	if(label_name not in Label):
		Label[label_name] = label_location


def insertVariable(variable_name : str, variable_location : int):
	global Variables
	if(variable_name not in Variables):
		Variables[variable_name] = variable_location


def checkSymbol(symbol_name : str) -> int:
	if(symbol_name == 'var'):
		return 1
	elif(symbol_name[-1] == ':'):
		return 2
	else:
		return 3

