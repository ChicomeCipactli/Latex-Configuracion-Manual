#!/usr/bin/python

import os 
import sys
from shutil import copyfile
import shutil

dir_path = os.path.dirname(os.path.realpath(__file__)) 
treeFile = "tree.files"          # archivo de árbol de ejercicios

flags = [
    "-D ",    # directorio 
    "-F ",    # archivo cualquiera
    "-T ",    # archivo .tex
]

tabspaces = 4
tex = ["ej", ".tex"]
# tabspaces = int(input("tabspaces: "))

if not os.path.isdir("ejercicios"):
    os.mkdir("ejercicios")
else:
    print("Ya existe la carpeta de ejercicios")
    sys.exit()
    # shutil.rmtree("ejercicios")
    # os.mkdir("ejercicios")

lines = []

if not os.path.isfile(treeFile):
    print("No encuentro el archivo tree.files")
    sys.exit()

with open(treeFile, "r") as f:
    for line in f.readlines():
        lines.append(line)

os.chdir("ejercicios")

class Line(object):
    def __init__(self, line):
        self.flag = "-F "
        for flag in flags:
            if flag in line:
                self.flag = flag

        self.string = line[:-1].split(self.flag, 1)[1]
        self.depth = int(line[:-1].split(self.flag, 1)[0].count(" ") / tabspaces)

elements = []

for line in lines:
    l = line.split("#")[0].replace(" ","")
    if l == "" or l == "\n":
        continue
    else:
        elements.append(Line(line))

curr_dir = []

depth = 0

ej_tex = open("/home/juamnito/Latex-Configuracion-Manual/Scripts/src/ej.tex", "r")

ejercicio_str = ej_tex.readlines()
ejercicio_str = "".join(ejercicio_str)

treeFile = open("tree.tex", "w")

treeFile.write("% árbol de archivos\n\n")

# for elem in elements:
#     print(elem.flag, elem.string, elem.depth)

for elem in elements:
    if elem.flag == flags[0]:
        if depth == elem.depth:
            curr_dir.append(elem.string)
            depth += 1
        elif depth < elem.depth:
            print("Invalid syntax for .files file")
            print("error in:", elem.flag + elem.string)
            sys.exit()
        else:
            # depth -= 1
            splits = depth - elem.depth
            for _ in range(splits):
                curr_dir.pop()
                depth -= 1
            curr_dir.append(elem.string)

    directory = "./" + "/".join(curr_dir)
    if not os.path.isdir(directory):
        os.mkdir(directory)
        print("mkdir", directory[2:])
        treeFile.write("\\section*{" + curr_dir[ len( curr_dir ) - 1 ] + "}\n")

    if elem.flag == flags[1]:
        for e in elem.string.split(" "):
            name = directory + "/" + e
            f = open(name, "w")
            f.close()
            name = name[2:]
            print("touch", name)
            if e[-4:] == ".tex":
                treeFile.write("\t\\input{ejercicios/" + name[:-4] + "}\n")

    if elem.flag == flags[2]:
        titles = elem.string.split(" ")
        for title in titles:
            name = directory + "/" + tex[0] + title + tex[1]
            f = open(name, "w")
            f.write(ejercicio_str)
            f.close()
            name = name[2:]
            if elem.depth == 0:
                name = name[1:]
            print("touch", name)
            treeFile.write("\t\\input{ejercicios/" + name[:-4] + "}\n")
            
treeFile.close()
