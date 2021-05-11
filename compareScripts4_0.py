# -*- coding: utf-8 -*-
"""
Created on *********

@author: 了不起的田所李
"""
import sys
from openpyxl import load_workbook
import csv
import pandas as pd
import re
from Bio import PDB
import os


filename = sys.argv[1]
nonsuffix_filename = filename.replace(".csv", "")
#  产生ali文件


def create_alifile(modelname, initial_num, protein_length, sequence):  # 产生ali文件，模型部分
    nonsuffix_modelname = modelname.replace(".pdb", "")
    sequence = sequence.replace("\n", "")
    with open(nonsuffix_filename + "-mult0.ali", "a+") as alifile:
        alifile.write("\n")
        alifile.write(">P1;" + "reset_" + nonsuffix_modelname + "\n")
        alifile.write("structureX:" + "reset_" + modelname + ":" + str(initial_num) + "  :A:+" + str(protein_length)
                      + " :A:::-1.00:-1.00\n")
        alifile.write(str("-" * int(initial_num - 1)) + sequence
                      + str("-" * abs(int(final_initial_num + final_protein_length - (initial_num + protein_length))))
                      + "*\n")
        # print(final_protein_length)
        # print(final_initial_num)
        # print(final_initial_num + final_protein_length)
        # print(abs(int(final_initial_num + final_protein_length - (initial_num + protein_length))))


def final_sentence(final_modelname, final_initial_num, final_protein_length, final_sequence):  # 继续写入ali
    nonsuffix_final_modelname = final_modelname.replace(".pdb", "")  # 为最后的pdb部分
    final_sequence = final_sequence.replace("\n", "")
    with open(nonsuffix_filename + "-mult0.ali", "a+") as alifile:
        alifile.write("\n")
        alifile.write(">P1;" + "reset_" + nonsuffix_final_modelname + "\n")
        alifile.write("structureX:" + "reset_" + final_modelname + ": " + str(final_initial_num)
                      + "  :A:+" + str(final_protein_length)
                      + " :A:::-1.00:-1.00\n")
        alifile.write(str("-" * abs(int(final_initial_num - 1)) + final_sequence) + "*\n")


def objectname(object_modelname, object_sequence):  # 继续写入ali部分，序列部分
    object_sequence = object_sequence.replace("\n", "")
    with open(nonsuffix_filename + "-mult0.ali", "a+") as alifile:
        alifile.write("\n")
        alifile.write(">P1;" + object_modelname + "\n")
        alifile.write("sequence:" + object_modelname + ":     : :     : ::: 0.00: 0.00\n")
        alifile.write(object_sequence + "*\n")

    with open(object_modelname + ".ali", "w+") as alifile:  # 为单独的序列生产出一个ali文件
        alifile.write("\n")
        alifile.write(">P1;" + object_modelname + "\n")
        alifile.write("sequence:" + object_modelname + ":     : :     : ::: 0.00: 0.00\n")
        alifile.write(object_sequence + "*\n")


def stringcounter(string):  # 统计字符串长度
    string_number = 0
    for number in string:
        string_number += 1
    # print("final_sequence_number:", string_number)
    return string_number


def sequence_search(keyword, text):  # 序列索引定位，定位initial-num
    # global initial
    # initial = None
    keyword = keyword.replace("\n", "")
    text = text.replace("\n", "")
    for number0 in re.finditer(keyword, text):
        # print(number0.group(), str(number0.span()))
        initial = int(number0.span()[0]) + 1
        pass
    # print(initial)
    return initial


def pdb2fasta(pdbfilename):  # 将一个pdb文件转换为fasta序列
    new_filename = pdbfilename.replace(".pdb", "")

    parser = PDB.PDBParser()
    structure = parser.get_structure(new_filename, pdbfilename)
    ppb = PDB.PPBuilder()

    for pp in ppb.build_peptides(structure):
        ppstring = pp.get_sequence()
    # print(new_filename, "转换序列为：", ppstring)
    return ppstring


def residue(modelname, addnum):  # 改变pdb文件整体的序列，根据ini数
    # if not os.path.exists(os.getcwd() + "/newpdb"):
    #     os.mkdir('newpdb')
    with open("reset_" + modelname, "w+") as newpdbfile:
        with open(modelname, "r") as pdbfile:
            string = pdbfile.readline()
            pdbfile.seek(0)  # 指针归位
            # print(string)
            num = string[23:26].strip()
            # print(num)
            for line in pdbfile:
                # print(line, end="")
                line_num = line[23:26].strip()
                if line_num != "":
                    new_line_num = int(line_num) + int(addnum) - int(num)
                # print(line[:6]+line[11:22]+str(new_line_num).rjust(4)+line[26:], end='')
                write_line = line[:12] + line[12:22] + str(new_line_num).rjust(4) + line[26:]
                del_num = "END\n " + str(new_line_num)
                # print(del_num)
                if write_line != del_num:
                    newpdbfile.write(write_line)
            newpdbfile.write("END")


if __name__ == '__main__':
    try:
        os.remove(nonsuffix_filename + "-mult0.ali")
        print("初始ali文件删除，开始运行")
    except FileNotFoundError:
        print("没有ali文件删除，开始运行")

    data = pd.read_csv(filename)
    data.dropna(axis=0, inplace=True)  # 删除带空值的行
    print(data)

    final_modelname = data.iloc[-1, 0]
    print("final_modelname", final_modelname)
    # final_sequence = data.iloc[-1, 1]
    final_sequence = str(pdb2fasta(final_modelname))
    final_sequence = final_sequence.replace("\n", "")
    final_protein_length = stringcounter(final_sequence)
    # print(final_modelname)
    print("final_sequence", final_sequence)
    # print(final_protein_length)
    object_modelname = data.iloc[0, 0]
    object_sequence = data.iloc[0, 1]  # 这个是初始序列，用于对字符串的全局搜索
    # object_sequence = object_sequence.replace("\n", "")
    print("object_sequence", object_sequence)
    final_initial_num = sequence_search(final_sequence, object_sequence)
    # print(final_initial_num)

    for i in range(1, data.iloc[:, 0].size - 1):  # 从结构文件2开始取，0是名字列表，1是模板列表，-1是最后的一个pdb，还就那个不要取
        exec("modelname = data.iloc[" + str(i) + ",0]")
        # exec("sequence = data.iloc[" + str(i) + ",1]")
        exec("sequence = str(pdb2fasta(modelname))")
        # print(modelname)
        print(modelname + "输出序列为：", sequence)
        sequence.replace("\n", "")  # 删除序列中可能存在的换行符
        protein_length = stringcounter(sequence)  # 读取序列中的字符串个数
        initial_num = sequence_search(sequence, object_sequence)
        create_alifile(modelname, initial_num, protein_length, sequence)
        residue(modelname, initial_num)
    final_sentence(final_modelname, final_initial_num, final_protein_length, final_sequence)
    residue(final_modelname, final_initial_num)
    objectname(object_modelname, object_sequence)
