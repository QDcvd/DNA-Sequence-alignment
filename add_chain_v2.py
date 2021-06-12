import sys
import os


modelname = sys.argv[1]
chain = str(sys.argv[2])

try:
    from modeller import *
    from modeller.automodel import *
except ModuleNotFoundError:
    print("错误：无法找到Modeller模块，正在自检安装Modeller模块...")
    os.system("conda config --add channels salilab")
    os.system("conda install modeller")

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
            # if line_A == "":
            #     line_A = line_A.replace("", chain + " ")
            # if line_A == "A":
            #     line_A = line_A.replace("A", chain + " ")
            line_A = line_A.replace(line_A, chain + " ")

                # new_line_num = int(line_num)
            # # print(line[:6]+line[11:22]+str(new_line_num).rjust(4)+line[26:], end='')
            write_line = line[:12] + line[12:21] + line_A + line[23:]
            # del_num = "END\n " + str(new_line_num)
            # print(del_num)
            # if write_line != del_num:
            newpdbfile.write(write_line)
        newpdbfile.write("END")

print("文件生成成功，将以：reset_" + modelname + "存在")

