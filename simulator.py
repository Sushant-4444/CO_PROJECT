import sys


def int_to_bin(num, bits):
    bin_of_num = ""
    bin_2_complement = ""
    if num < 0:
        bin_of_num = str(bin(int(num))[3:])
        if bin_of_num[0] == "1":
            bin_of_num = "0" + bin_of_num

        for i in range(len(bin_of_num)):
            if bin_of_num[i] == "0":
                bin_2_complement = bin_2_complement + "1"

            else:
                bin_2_complement = bin_2_complement + "0"

        for i in range(len(bin_2_complement) - 1, -(len(bin_2_complement) + 1), -1):
            if bin_2_complement[i] == "0":
                bin_2_complement = (
                    bin_2_complement[:i] + "1" + bin_2_complement[i + 1 :]
                )
                break
            else:
                bin_2_complement = (
                    bin_2_complement[:i] + "0" + bin_2_complement[i + 1 :]
                )

        bin_of_num = bin_2_complement
        for i in range(bits - len(bin_of_num)):
            bin_of_num = "1" + bin_of_num

    if num >= 0:
        bin_of_num = str(bin(int(num))[2:])
        for i in range(bits - len(bin_of_num)):
            bin_of_num = "0" + bin_of_num
    return bin_of_num


def bin_to_int(bin_num):
    if bin_num[0] == "0":
        return int(bin_num, 2)
    else:
        bin_num = bin_num[1:]
        bin_2_complement = ""
        for i in range(len(bin_num)):
            if bin_num[i] == "0":
                bin_2_complement = bin_2_complement + "1"

            else:
                bin_2_complement = bin_2_complement + "0"

        for i in range(len(bin_2_complement) - 1, -(len(bin_2_complement) + 1), -1):
            if bin_2_complement[i] == "0":
                bin_2_complement = (
                    bin_2_complement[:i] + "1" + bin_2_complement[i + 1 :]
                )
                break
            else:
                bin_2_complement = (
                    bin_2_complement[:i] + "0" + bin_2_complement[i + 1 :]
                )

        bin_num = bin_2_complement
        return -int(bin_num, 2)


def bin_to_hex(bin_num):
    hex_num = hex(int(bin_num, 2))
    return hex_num[0:2] + "000" + hex_num[2:]


register_values = {
    "PC": int_to_bin(0, 32),
    "00000": int_to_bin(0, 32),
    "00001": int_to_bin(0, 32),
    "00010": "00000000000000000000000100000000",
    "00011": int_to_bin(0, 32),
    "00100": int_to_bin(0, 32),
    "00101": int_to_bin(0, 32),
    "00110": int_to_bin(0, 32),
    "00111": int_to_bin(0, 32),
    "01000": int_to_bin(0, 32),
    "01001": int_to_bin(0, 32),
    "01010": int_to_bin(0, 32),
    "01011": int_to_bin(0, 32),
    "01100": int_to_bin(0, 32),
    "01101": int_to_bin(0, 32),
    "01110": int_to_bin(0, 32),
    "01111": int_to_bin(0, 32),
    "10000": int_to_bin(0, 32),
    "10001": int_to_bin(0, 32),
    "10010": int_to_bin(0, 32),
    "10011": int_to_bin(0, 32),
    "10100": int_to_bin(0, 32),
    "10101": int_to_bin(0, 32),
    "10110": int_to_bin(0, 32),
    "10111": int_to_bin(0, 32),
    "11000": int_to_bin(0, 32),
    "11001": int_to_bin(0, 32),
    "11010": int_to_bin(0, 32),
    "11011": int_to_bin(0, 32),
    "11100": int_to_bin(0, 32),
    "11101": int_to_bin(0, 32),
    "11110": int_to_bin(0, 32),
    "11111": int_to_bin(0, 32),
}

data_memory = {
    "0x00010000": int_to_bin(0, 32),
    "0x00010004": int_to_bin(0, 32),
    "0x00010008": int_to_bin(0, 32),
    "0x0001000c": int_to_bin(0, 32),
    "0x00010010": int_to_bin(0, 32),
    "0x00010014": int_to_bin(0, 32),
    "0x00010018": int_to_bin(0, 32),
    "0x0001001c": int_to_bin(0, 32),
    "0x00010020": int_to_bin(0, 32),
    "0x00010024": int_to_bin(0, 32),
    "0x00010028": int_to_bin(0, 32),
    "0x0001002c": int_to_bin(0, 32),
    "0x00010030": int_to_bin(0, 32),
    "0x00010034": int_to_bin(0, 32),
    "0x00010038": int_to_bin(0, 32),
    "0x0001003c": int_to_bin(0, 32),
    "0x00010040": int_to_bin(0, 32),
    "0x00010044": int_to_bin(0, 32),
    "0x00010048": int_to_bin(0, 32),
    "0x0001004c": int_to_bin(0, 32),
    "0x00010050": int_to_bin(0, 32),
    "0x00010054": int_to_bin(0, 32),
    "0x00010058": int_to_bin(0, 32),
    "0x0001005c": int_to_bin(0, 32),
    "0x00010060": int_to_bin(0, 32),
    "0x00010064": int_to_bin(0, 32),
    "0x00010068": int_to_bin(0, 32),
    "0x0001006c": int_to_bin(0, 32),
    "0x00010070": int_to_bin(0, 32),
    "0x00010074": int_to_bin(0, 32),
    "0x00010078": int_to_bin(0, 32),
    "0x0001007c": int_to_bin(0, 32),
}


def simulator(instruction):

    if instruction[25:32] == "0110011":
        opcode = instruction[25:32]
        funct7 = instruction[0:7]
        rs2 = instruction[7:12]
        rs1 = instruction[12:17]
        funct3 = instruction[17:20]
        rd = instruction[20:25]
        register_values["PC"] = int_to_bin(int(register_values["PC"], 2) + 4, 32)
        if funct7 == "0000000":
            if funct3 == "000":
                print(register_values["00000"])
                register_values[rd] = int_to_bin(
                    bin_to_int(register_values[rs1]) + bin_to_int(register_values[rs2]),
                    32,
                )
            elif funct3 == "001":
                register_values[rd] = int_to_bin(
                    int(register_values[rs1], 2) << int(register_values[rs2][27:32], 2),
                    32,
                )
            elif funct3 == "010":
                if bin_to_int(register_values[rs1]) < bin_to_int(register_values[rs2]):
                    register_values[rd] = int_to_bin(1, 32)
            elif funct3 == "011":
                if int(register_values[rs1], 2) < int(register_values[rs2], 2):
                    register_values[rd] = int_to_bin(1, 32)
            elif funct3 == "100":
                register_values[rd] = int_to_bin(
                    int(register_values[rs1], 2) ^ int(register_values[rs2], 2), 32
                )
            elif funct3 == "101":
                register_values[rd] = int_to_bin(
                    int(register_values[rs1], 2) >> int(register_values[rs2][27:32], 2),
                    32,
                )
            elif funct3 == "110":
                register_values[rd] = int_to_bin(
                    int(register_values[rs1], 2) | int(register_values[rs2], 2), 32
                )
            elif funct3 == "111":
                register_values[rd] = int_to_bin(
                    int(register_values[rs1], 2) & int(register_values[rs2], 2), 32
                )
            else:
                print("Invalid R-type instruction")

        elif funct7 == "0100000":
            if funct3 == "000":
                register_values[rd] = int_to_bin(
                    bin_to_int(register_values[rs1]) - bin_to_int(register_values[rs2]),
                    32,
                )
            else:
                print("Invalid R-type instruction")
    elif (
        instruction[25:32] == "0000011"
        or instruction[25:32] == "0010011"
        or instruction[25:32] == "1100111"
    ):
        opcode = instruction[25:32]
        imm = instruction[0:12]
        rs1 = instruction[12:17]
        funct3 = instruction[17:20]
        rd = instruction[20:25]
        if opcode == "0010011":
            register_values["PC"] = int_to_bin(int(register_values["PC"], 2) + 4, 32)
            if funct3 == "000":
                register_values[rd] = int_to_bin(
                    bin_to_int(register_values[rs1]) + bin_to_int(imm), 32
                )
            elif funct3 == "001":
                register_values[rd] = int_to_bin(
                    int(register_values[rs1], 2) < int(imm, 2), 32
                )
        elif opcode == "1100111":
            register_values[rd] = int_to_bin(int(register_values["PC"], 2) + 4, 32)
            register_values["PC"] = int_to_bin(
                bin_to_int(register_values[rs1]) + bin_to_int(imm), 32
            )
        elif opcode == "0000011":
            register_values["PC"] = int_to_bin(int(register_values["PC"], 2) + 4, 32)
            register_values[rd] = data_memory[
                bin_to_hex(
                    int_to_bin(bin_to_int(register_values[rs1]) + bin_to_int(imm), 32)
                )
            ]

        else:
            print("Invalid I-type instruction")

    elif instruction[25:32] == "0100011":
        opcode = instruction[25:32]
        imm = instruction[0:7] + instruction[20:24]
        rs2 = instruction[7:12]
        rs1 = instruction[12:17]
        funct3 = instruction[17:20]
        data_memory[
            bin_to_hex(
                int_to_bin(bin_to_int(register_values[rs1]) + bin_to_int(imm), 32)
            )
        ] = register_values[rs2]
        register_values["PC"] = int_to_bin(bin_to_int(register_values["PC"]) + 4, 32)

    elif instruction[25:32] == "1100011":
        opcode = instruction[25:32]
        imm = instruction[0] + instruction[24] + instruction[1:7] + instruction[20:24]
        rs2 = instruction[7:12]
        rs1 = instruction[12:17]
        funct3 = instruction[17:20]

        if funct3 == "000":
            if bin_to_int(register_values[rs1]) == bin_to_int(register_values[rs2]):
                register_values["PC"] = int_to_bin(
                    bin_to_int(register_values["PC"]) + bin_to_int(imm + "0"), 32
                )
            else:
                register_values["PC"] = int_to_bin(
                    int(register_values["PC"], 2) + 4, 32
                )
        elif funct3 == "001":
            if register_values[rs1] != register_values[rs2]:
                register_values["PC"] = int_to_bin(
                    int(register_values["PC"], 2) + bin_to_int(imm + "0"), 32
                )
            else:
                register_values["PC"] = int_to_bin(
                    int(register_values["PC"], 2) + 4, 32
                )
        elif funct3 == "100":
            if bin_to_int(register_values[rs1]) < bin_to_int(register_values[rs2]):
                register_values["PC"] = int_to_bin(
                    int(register_values["PC"], 2) + bin_to_int(imm + "0"), 32
                )
            else:
                register_values["PC"] = int_to_bin(
                    int(register_values["PC"], 2) + 4, 32
                )
        elif funct3 == "101":
            if bin_to_int(register_values[rs1]) >= bin_to_int(register_values[rs2]):
                register_values["PC"] = int_to_bin(
                    int(register_values["PC"], 2) + bin_to_int(imm + "0"), 32
                )
            else:
                register_values["PC"] = int_to_bin(
                    int(register_values["PC"], 2) + 4, 32
                )
        elif funct3 == "110":
            if int(register_values[rs1], 2) < int(register_values[rs2], 2):
                register_values["PC"] = int_to_bin(
                    int(register_values["PC"], 2) + bin_to_int(imm + "0"), 32
                )

            else:
                register_values["PC"] = int_to_bin(
                    int(register_values["PC"], 2) + 4, 32
                )
        elif funct3 == "111":
            if int(register_values[rs1], 2) >= int(register_values[rs2], 2):
                register_values["PC"] = int_to_bin(
                    int(register_values["PC"], 2) + bin_to_int(imm + "0"), 32
                )
            else:
                register_values["PC"] = int_to_bin(
                    int(register_values["PC"], 2) + 4, 32
                )

        else:
            print("Invalid B-type instruction")

    elif instruction[25:32] == "0110111":
        imm = instruction[0:20]
        rd = instruction[20:25]
        register_values[rd] = int_to_bin(bin_to_int(imm + "000000000000"), 32)
        register_values["PC"] = int_to_bin(int(register_values["PC"], 2) + 4, 32)

    elif instruction[25:32] == "0010111":
        imm = instruction[0:20]
        rd = instruction[20:25]
        register_values[rd] = int_to_bin(
            bin_to_int(register_values["PC"]) + (bin_to_int(imm + "000000000000")), 32
        )
        register_values["PC"] = int_to_bin(int(register_values["PC"], 2) + 4, 32)

    elif instruction[25:32] == "1101111":
        imm = (
            instruction[0]
            + instruction[12:20]
            + instruction[11]
            + instruction[1:11]
            + "0"
        )
        rd = instruction[20:25]
        register_values[rd] = int_to_bin(int(register_values["PC"], 2) + 4, 32)
        register_values["PC"] = int_to_bin(
            bin_to_int(register_values["PC"]) + bin_to_int(imm), 32
        )


# instructions = [
# "00000000000000000000010010110011",
# "00000000000000000000100100110011",
# "00000000000100000000010010010011",
# "00000001000000000000100100010011",
# "00000001001001001001010010110011",
# "00000000101100000000101010010011",
# "00000001010101001010000000100011",
# "00000000000001001010100100000011",
# "00000000010001001000010010010011",
# "00000000000100000000100110010011",
# "00000001001110010111100100110011",
# "00000001001000000000100001100011",
# "00000000001100000000101000010011",
# "00000001010001001010000000100011",
# "00000000000000000000000001100011",
# "00000000001000000000101000010011",
# "00000001010001001010000000100011",
# "00000000000000000000000001100011"
#     ]
# instructions = [
# "00000000000000000000010000110011",
# "00000000000100000000010010010011",
# "00000000000000000000100100110011",
# "00000000011000000000100110010011",
# "00000001100000000000000011101111",
# "00000000000001001000010000110011",
# "00000000000010010000010010110011",
# "11111111111110011000100110010011",
# "11111110000010011001100011100011",
# "00000000000000000000000001100011",
# "00000000100101000000100100110011",
# "00000000000000001000000001100111",
# "00000000000000000000000001100011"
# ]

# instructions = [
# "00000000001000000000010000010011",
# "00000001000000000000010010010011",
# "00000000000100000000100100010011",
# "00000000001100000000100110010011",
# "00000000100110010001100100110011",
# "00000000000100000000001010010011",
# "00000000100010010010000000100011",
# "00000000010010010000100100010011",
# "01000000010101000000010000110011",
# "01000000010110011000100110110011",
# "00000010000010011000001001100011",
# "11111110000001000001010011100011",
# "00000000100010010010000000100011",
# "00000000010010010000100100010011",
# "00000000000100000000001010010011",
# "01000000010101000000010000110011",
# "00000001110100000000001010010011",
# "00000000010101000101010000110011",
# "11111100000001000001011011100011",
# "00000000000000000000000001100011"
# ]
# instructions = [
#     "00000000000000000000010000110011",
# "11111111100100000000010010010011",
# "00000000000000010000010000110111",
# "00000000100101000010000000100011",
# "00000000000101001000010010010011",
# "00000000010001000000010000010011",
# "00000000100101000010000000100011",
# "00000000000000010000010000010111",
# "00000000000101001000010010010011",
# "00000000100101000010000000100011",
# "00000000010001000000010000010011",
# "00000000000101001000010010010011",
# "00000000100101000010000000100011",
# "00000000000000000000000001100011",
# ]

instructions = []
index = int(0)
while index in range(0, len(instructions)):
    if instructions[index] == "00000000000000000000000001100011":
        simulator(instructions[index])
        with open("output11.txt", "a") as file:
            for key, value in register_values.items():
                file.write("0b" + value + " ")
            # for key, value in memory_values.items():
            # file.write(key + " " + str(value) + "\n")")
            file.write("\n")
            index = int((bin_to_int(register_values["PC"]) / 4))
        break
    else:
        simulator(instructions[index])
        with open("output11.txt", "a") as file:
            for key, value in register_values.items():
                file.write("0b" + value + " ")
            # for key, value in memory_values.items():
            # file.write(key + " " + str(value) + "\n")")
            file.write("\n")
            index = int((bin_to_int(register_values["PC"]) / 4))
            print(index)
with open("output11.txt", "a") as file:
    for key, value in data_memory.items():
        file.write(key + ":" + "0b" + value + "\n")
