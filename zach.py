# coverts binary to decimal. EX: bin_to_dec("1001011") = 75
def bin_to_dec(number=""):
    # init return value to 0
    decimal_number = 0
    # 5 ** 3 = 5 to the power of  3 = 125

    # this if is for error checking
    if (len(number) <= 0):
        return 0;

    # power = the highest binary digit in decimal EX if 1001011, power = 2 ** 6
    power = 2 ** (len(number) - 1)

    # traverse through the binary string number
    for i in number:
        # if it is one, add power to the final decimal number. Else do not
        if (i == '1'):
            decimal_number = decimal_number + power

        # reduce the power by two to switch to the next digit
        power = power / 2

    # return the decimal number
    return decimal_number


################################################################
def get_spaced_instr(instr=""):
    # example '00100000000000010000000000001010' --> '10001011 000 00010 00000 00000 100011'
    temp = "" + instr[0:8]
    temp = temp + " "
    temp = temp + instr[8:11]
    temp = temp + " "
    temp = temp + instr[11:16]
    temp = temp + " "
    temp = temp + instr[16:21]
    temp = temp + " "
    temp = temp + instr[21:26]
    temp = temp + " "
    temp = temp + instr[26:32]
    return temp


def btype(arg1, arg1str, machineCode=""):
    arg1.append(machineCode[7:32])
    temp = "#"
    temp = temp + str(bin_to_dec(machineCode[7:32]))
    arg1str.append(temp)


# function
def c_btype(arg1, arg1str, arg2, arg2str, machineCode=""):
    arg1.append(machineCode[27:32])
    temp = "R"
    temp = temp + str(bin_to_dec(machineCode[27:32]))
    arg1str.append(temp)
    arg2.append(machineCode[9:27])
    temp = "#"
    temp = temp + str(bin_to_dec(machineCode[9:27]))
    arg2str.append(temp)


# function
def imtype(arg1, arg1str, arg2, arg2str, arg3, arg3str, machineCode=""):
    arg1.append(machineCode[27:32])
    temp = "R"
    temp = temp + str(bin_to_dec(machineCode[27:32]))
    arg1str.append(temp)
    arg2.append(machineCode[11:27])
    temp = ""
    temp = temp + str(bin_to_dec(machineCode[11:27]))
    arg2str.append(temp)
    arg3.append(machineCode[9:11])
    temp = "LSL " + str(bin_to_dec(machineCode[9:11]) * 16)
    arg3Str.append(temp)


# function
def itype(arg1, arg1str, arg2, arg2str, arg3, arg3str, machineCode=""):
    arg3.append(machineCode[10:22])
    temp = "#"
    temp = temp + str(bin_to_dec(machineCode[10:22]))
    arg3str.append(temp)
    arg2.append(machineCode[22:27])
    temp = "R"
    temp = temp + str(bin_to_dec(machineCode[22:27]))
    arg2str.append(temp)
    arg1.append(machineCode[27:32])
    temp = "R"
    temp = temp + str(bin_to_dec(machineCode[27:32]))
    arg1str.append(temp)


# function
def rtype(arg1, arg1str, arg2, arg2str, arg3, arg3str, machineCode=""):
    op = bin_to_dec(i[0:11])
    if (op == 1690 or op == 1691):  # if LSR or LSL
        arg3.append(machineCode[16:22])
        temp = "#"
        temp = temp + str(bin_to_dec(machineCode[16:22]))
    else:
        arg3.append(machineCode[11:16])
        temp = "R"
        temp = temp + str(bin_to_dec(machineCode[11:16]))
    arg3str.append(temp)
    arg2.append(machineCode[23:27])
    temp = "R"
    temp = temp + str(bin_to_dec(machineCode[23:27]))
    arg2str.append(temp)
    arg1.append(machineCode[27:32])
    temp = "R"
    temp = temp + str(bin_to_dec(machineCode[27:32]))
    arg1str.append(temp)


# function
def dtype(arg1, arg1str, arg2, arg2str, arg3, arg3str, machineCode=""):
    arg3.append(machineCode[11:20])
    temp = "#"
    temp = temp + str(bin_to_dec(machineCode[11:20]))
    temp = temp + "]"
    arg3str.append(temp)
    arg2.append(machineCode[22:27])
    temp = "[R"
    temp = temp + str(bin_to_dec(machineCode[22:27]))
    arg2str.append(temp)
    arg1.append(machineCode[28:32])
    temp = "R"
    temp = temp + str(bin_to_dec(machineCode[28:32]))
    arg1str.append(temp)


# function
################################################################
# data structures
################################################################
opcodeStr = []  # <type 'list'>: ['Invalid Instruction', 'ADDI', 'SW', 'Invalid Instruction', 'LW', 'BLTZ', 'SLL',...]
validStr = []  # <type 'list'>: ['N', 'Y', 'Y', 'N', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y',...]
instrSpaced = []  # <type 'list'>: ['0 01000 00000 00001 00000 00000 001010', '1 01000 00000 00001 00000 00000 001010',...]
arg1 = []  # <type 'list'>: [0, 0, 0, 0, 0, 1, 1, 10, 10, 0, 3, 4, 152, 4, 10, 1, 0, 112, 0]
arg2 = []  # <type 'list'>: [0, 1, 1, 0, 1, 0, 10, 3, 4, 5, 0, 5, 0, 5, 6, 1, 1, 0, 0]
arg3 = []  # <type 'list'>: [0, 10, 264, 0, 264, 48, 2, 172, 216, 260, 8, 6, 0, 6, 172, -1, 264, 0, 0]
arg1Str = []  # <type 'list'>: ['', '\tR1', '\tR1', '', '\tR1', '\tR1', '\tR10', '\tR3', '\tR4', .....]
arg2Str = []  # <type 'list'>: ['', ', R0', ', 264', '', ', 264', ', #48', ', R1', ', 172', ', 216', ...]
arg3Str = []  # <type 'list'>: ['', ', #10', '(R0)', '', '(R0)', '', ', #2', '(R10)', '(R10)', '(R0)',...]
mem = []  # <type 'list'>: [-1, -2, -3, 1, 2, 3, 0, 0, 5, -5, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
binMem = []  # <type 'list'>: ['11111111111111111111111111111111', '11111111111111111111111111111110', ...]
valid = []
opcode = []
isData = []
################################################################
# open and read file
machineCodeFile = open("test2_bin.txt")
machineCode = machineCodeFile.readlines()
machineCodeFile.close()

memCurrent = 96
data_section = False

for i in machineCode:
    op = bin_to_dec(i[0:11])
    instrSpaced.append(get_spaced_instr(i))
    mem.append(memCurrent)                  ################################# WTF DIS FOR???????????????
    memCurrent = memCurrent + 4

    if (data_section == False):
        isData.append(False)
        if (op >= 160 and op <= 191):
            opcodeStr.append("B")
            opcode.append(i[0:6])
            btype(arg1, arg1Str, i)
            arg2Str.append("")
            arg2.append("")
            arg3Str.append("")
            arg3.append("")
            validStr.append('Y')
        elif (op == 1104):
            opcodeStr.append("AND")
            opcode.append(i[0:11])
            rtype(arg1, arg1Str, arg2, arg2Str, arg3, arg3Str, i)
            validStr.append('Y')
        elif (op == 1112):
            opcodeStr.append("ADD")
            opcode.append(i[0:11])
            rtype(arg1, arg1Str, arg2, arg2Str, arg3, arg3Str, i)
            validStr.append('Y')
        elif (op == 1160 or op == 1161):
            opcodeStr.append("ADDI")
            opcode.append(i[0:10])
            itype(arg1, arg1Str, arg2, arg2Str, arg3, arg3Str, i)
            validStr.append('Y')
        elif (op == 1360):
            opcodeStr.append("ORR")
            opcode.append(i[0:11])
            rtype(arg1, arg1Str, arg2, arg2Str, arg3, arg3Str, i)
            validStr.append('Y')
        elif (op >= 1440 and op <= 1447):
            opcodeStr.append("CBZ")
            opcode.append(i[0:8])
            c_btype(arg1, arg1Str, arg2, arg2Str, i)
            arg3Str.append("")
            arg3.append("")
            validStr.append('Y')
        elif (op >= 1448 and op <= 1455):
            opcodeStr.append("CBNZ")
            opcode.append(i[0:8])
            c_btype(arg1, arg1Str, arg2, arg2Str, i)
            arg3Str.append("")
            arg3.append("")
            validStr.append('Y')
        elif (op == 1624):
            opcodeStr.append("SUB")
            opcode.append(i[0:11])
            rtype(arg1, arg1Str, arg2, arg2Str, arg3, arg3Str, i)
            validStr.append('Y')
        elif (op == 1672 or op == 1673):
            opcodeStr.append("SUBI")
            opcode.append(i[0:10])
            itype(arg1, arg1Str, arg2, arg2Str, arg3, arg3Str, i)
            validStr.append('Y')
        elif (op >= 1684 and op <= 1687):
            opcodeStr.append("MOVZ")
            opcode.append(i[0:9])
            imtype(arg1, arg1Str, arg2, arg2Str, arg3, arg3Str, i)
            validStr.append('Y')
        elif (op >= 1940 and op <= 1943):
            opcodeStr.append("MOVK")
            opcode.append(i[0:9])
            imtype(arg1, arg1Str, arg2, arg2Str, arg3, arg3Str, i)
            validStr.append('Y')
        elif (op == 1690):
            opcodeStr.append("LSR")
            opcode.append(i[0:11])
            rtype(arg1, arg1Str, arg2, arg2Str, arg3, arg3Str, i)
            validStr.append('Y')
        elif (op == 1691):
            opcodeStr.append("LSL")
            opcode.append(i[0:11])
            rtype(arg1, arg1Str, arg2, arg2Str, arg3, arg3Str, i)
            validStr.append('Y')
        elif (op == 1984):
            opcodeStr.append("STUR")
            opcode.append(i[0:11])
            dtype(arg1, arg1Str, arg2, arg2Str, arg3, arg3Str, i)
            validStr.append('Y')
        elif (op == 1986):
            opcodeStr.append("LDUR")
            opcode.append(i[0:11])
            dtype(arg1, arg1Str, arg2, arg2Str, arg3, arg3Str, i)
            validStr.append('Y')
        elif (op == 2038):
            opcodeStr.append("BREAK")
            opcode.append(i[0:11])
            arg1.append("")
            arg2.append("")
            arg3.append("")
            arg1Str.append("")
            arg2Str.append("")
            arg3Str.append("")
            validStr.append('Y')
            data_section = True
        else:
            opcodeStr.append("error")
            opcode.append("")
            arg1.append("")
            arg2.append("")
            arg3.append("")
            arg1Str.append("")
            arg2Str.append("")
            arg3Str.append("")
            validStr.append('N')
    else:
        isData.append(True)
        arg1.append("")
        arg2.append("")
        arg3.append("")
        arg1Str.append("")
        arg2Str.append("")
        arg3Str.append("")
        validStr.append('Y')

elementCount = 0
dataMem = 0
for i in machineCode:
    if (isData[elementCount] == False):
        if (arg2Str[elementCount] != ""):
            comma1 = ", "
        else:
            comma1 = ""
        if (arg3Str[elementCount] != ""):
            comma2 = ", "
        else:
            comma2 = ""
        print instrSpaced[elementCount] + "\t" + str(mem[elementCount]) + "\t" + opcodeStr[elementCount] + " " + \
              arg1Str[elementCount] + comma1 + arg2Str[elementCount] + comma2 + arg3Str[elementCount]
    else:
        dataMem = dataMem - 1
        print i + "\t" + str(mem[elementCount]) + " " + str(dataMem)
    elementCount = elementCount + 1

