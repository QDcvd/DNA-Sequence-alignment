from modeller import *
from modeller.automodel import *
import sys

alifile = sys.argv[1]
sequence = sys.argv[2]
# pdbfilename1 = sys.argv[3]
# pdbfilename2 = sys.argv[4]
# pdbfilename3 = sys.argv[5]

file_num = sys.argv[3]
pdbfile_list = []
for pdbfile_num in range(4, 2 * int(file_num) + 1):
    print(pdbfile_num)
    exec("pdbfilename" + str(pdbfile_num) + "=" + "sys.argv[" + str(pdbfile_num) + "]")
    exec("pdbfile_list.append(pdbfilename" + str(pdbfile_num) + ")")

pdbfile_list_string = str(pdbfile_list)
# pdbfile_list_string = pdbfile_list_string.replace("'", "")
pdbfile_list_string = pdbfile_list_string.replace("[", "")
pdbfile_list_string = pdbfile_list_string.replace("]", "")

env = environ()
a = automodel(env, alnfile=alifile + '.ali',
              knowns=(eval(pdbfile_list_string)), sequence=sequence)
a.starting_model = 1
a.ending_model = 5
a.make()
