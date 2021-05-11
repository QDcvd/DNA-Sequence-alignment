from modeller import *
from modeller.automodel import *
import sys

modelname = sys.argv[1]


with open("reset_" + modelname, "w+") as newpdbfile:
    with open(modelname, "r") as pdbfile:
        string = pdbfile.readline()
        pdbfile.seek(0)  # 指针归位
        # print(string)
        num = string[23:26].strip()
        # print(num)
        for line in pdbfile:
            # print(line, end="")
            line_A = line[21:23].strip()
            print(line_A)
            if line_A == "":
                line_A = line_A.replace("", "A ")
                # new_line_num = int(line_num)
            # # print(line[:6]+line[11:22]+str(new_line_num).rjust(4)+line[26:], end='')
            write_line = line[:12] + line[12:21] + line_A + line[23:]
            # del_num = "END\n " + str(new_line_num)
            # print(del_num)
            # if write_line != del_num:
            newpdbfile.write(write_line)
        newpdbfile.write("END")

