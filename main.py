import pdb

def convertResultToDots(result):
	DotsResult = ""
	if result <= 0:
		return ""
	else:
		for i in range(0,result):
			DotsResult += "."
	print(DotsResult)


def calculate(string):
	result = ""
	c1 = 0
	c2 = 0
	operators = string.split(" ")
	for char in operators[0]:
		c1 += 1
	for char in operators[2]:
		c2 += 1
	if operators[1] == "-":
		result = c1 - c2
		convertResultToDots(result)
	if operators[1] == "+":
		result = c1 + c2
		convertResultToDots(result)
	if operators[1] == "/":
		result = c1 / c2
		convertResultToDots(result)
	if operators[1] == "*":
		result = c1 * c2
		convertResultToDots(result)



while True:
	calculateThis = input("")
	calculate(calculateThis)





