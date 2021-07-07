def endx():
	if feld[1] == "x" and feld[2] == "x" and feld[3] == "x":
		return True
	elif feld[4] == "x" and feld[5] == "x" and feld[6] == "x":
		return True
	elif feld[7] == "x" and feld[8] == "x" and feld[9] == "x":
		return True
	elif feld[1] == "x" and feld[4] == "x" and feld[7] == "x":
		return True
	elif feld[2] == "x" and feld[5] == "x" and feld[8] == "x":
		return True
	elif feld[3] == "x" and feld[6] == "x" and feld[9] == "x":
		return True
	elif feld[1] == "x" and feld[5] == "x" and feld[9] == "x":
		return True
	elif feld[3] == "x" and feld[5] == "x" and feld[7] == "x":
		return True
	else:
		return False

def endo():
	if feld[1] == "o" and feld[2] == "o" and feld[3] == "o":
		return True
	elif feld[4] == "o" and feld[5] == "o" and feld[6] == "o":
		return True
	elif feld[7] == "o" and feld[8] == "o" and feld[9] == "o":
		return True
	elif feld[1] == "o" and feld[4] == "o" and feld[7] == "o":
		return True
	elif feld[2] == "o" and feld[5] == "o" and feld[8] == "o":
		return True
	elif feld[3] == "o" and feld[6] == "o" and feld[9] == "o":
		return True
	elif feld[1] == "o" and feld[5] == "o" and feld[9] == "o":
		return True
	elif feld[3] == "o" and feld[5] == "o" and feld[7] == "o":
		return True
	else:
		return False



def win():
	if endx() == True:
		print("X won!")
		exit()
	elif endo() == True:
		print("O won!")
		exit()
	else:
		pass


feld = [" ",
		"1", "2", "3", 
		"4", "5", "6", 
		"7", "8", "9"]

def field():
	print (feld[1] + "|" + feld[2] + "|" + feld[3] )
	print (feld[4] + "|" + feld[5] + "|" + feld[6] )
	print (feld[7] + "|" + feld[8] + "|" + feld[9] )

def rx(n):
	if feld[n] != "o":
		feld[n] = "x"

def ro(n):
	if feld[n] != "x":
		feld[n] = "o"

field()

r1 = int(input(
"X's turn!"
	))


rx(r1)
field()
win()

r2 = int(input(
"O's turn!"
	))

ro(r2)
field()
win()

r3 = int(input(
"X's turn!"
	))


rx(r3)
field()
win()

r4 = int(input(
"O's turn!"
	))

ro(r4)
field()
win()

r5 = int(input(
"X's turn!"
	))


rx(r5)
field()
win()

r6 = int(input(
"O's turn!"
	))


ro(r6)
field()
win()

r7 = int(input(
"X's turn!"
	))


rx(r7)
field()
win()

r8 = int(input(
"O's turn!"
	))


ro(r8)
field()
win()

r9 = int(input(
"X's turn!"
	))


rx(r9)
field()
win()


print("Draw!")