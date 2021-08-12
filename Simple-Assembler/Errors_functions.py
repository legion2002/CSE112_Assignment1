import Symbol_Table as st
import error as er
import opcode as op
import main 

def misuseOfLabelsAndVariables():
	for variable_name in st.Variables:
		if(variable_name in st.Label):
			print(er.error_file["f"])
			exit()

	for label_name in st.Label:
		if(label_name in st.Variables):
			print(er.error_file["f"])
			exit()


def errorCheckImm(immediate_value : str):
	if(immediate_value[0] != "$"):
		print(er.error_file["k"])
		exit()
	if(not(immediate_value >= 0 and immediate_value <= 255)):
		print(er.error_file["e"])
		exit()

def typoInInstruction(line_number : int):
	print(er.error_file["a"])
	exit()

def VariablesInBetween():
	flag = 0
	for instruction in main.instructions_file:
		if(instruction[0] != "var"):
			flag +=1 
		elif(instruction[0] == "var" and flag > 0):
			print(er.error_file["g"])
			exit()

def GeneralError():
	print(er.error_file["k"])
	exit()

def TyposInRegName(reg_name : str):
	if(reg_name not in op.registers.keys()):
		print(er.error_file["a"])
		exit()

def checkLabelAndVariableNames():
	for label_name in st.Label:
		if(label_name in op.type_opcode.keys()):
			print(er.error_file["k"])
			exit()

	for var_name in st.Variables:
		if(var_name in op.type_opcode.keys()):
			print(er.error_file["k"])
			exit()

def useOfUndefinedLabel(label_name : str):
	if(label_name not in st.Label):
		print(er.error_file["c"])
		exit()

def useOfUndefinedVariable(var_name : str):
	if(var_name not in st.Variables):
		print(er.error_file["b"])
		exit()








