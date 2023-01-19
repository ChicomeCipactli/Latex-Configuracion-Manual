#! /usr/bin/python

import os, sys, shutil

# source code

from configreader import reader
import custom_dirs

# defoults
flags = {
        "dir": "-D ",
        "file": "-F ",
        "tex_file": "-T "
}

tabspaces = 4
tex = ["ej", "tex"]

exercises_dir_name = "ejercicios"

def find_tree_files_config():
    tree_files = []

        # Look for .files config files
    for f in os.listdir():
        if f.split(".")[-1] == "files":
            tree_files.append(f)

        # give preference to tree.files file
    if "tree.files" in tree_files:
        return True, "tree.files"
    if len(tree_files) > 0:
        return True, tree_files[0]
    else:
        return False, "" # if its empty

def make_exercises_dir(forced=False, exercises_dir_name=exercises_dir_name):
    if not os.path.isdir(exercises_dir_name):
        os.mkdir(exercises_dir_name)
    elif forced:
        print("Overwriting the", exercises_dir_name, "directory")
        shutil.rmtree(exercises_dir_name)
        os.mkdir(exercises_dir_name)
    else:
        sys.exit()

# Reading configuration file

def read_tree_files_config(tree_files):
    tf = open(tree_files, "r")
    lines = tf.readlines()
    tf.close()

    return lines

# Class Line: argument and parameters
# expected a flag and filenames as parameters
# also a reasonable depth 

class Line(object):
    def __init__(self, line):
        self.flag = "-F"
        for flag in flags.values():
            if flag in line:
                self.flag = flag

                    # [:-1] to delete the "\n"
                    # split the flag and the rest is the parameter
                    # make sure that there is no other flag in 
                    # the same line.
                    # If there is other, it will be threated as 
                    # a filename
        line_split = line[:-1].split(self.flag, 1)
        self.parameter_files = line_split[1]

                    # count the number of spaces before
                    # the flag in the line
        spaces = line_split[0].count(" ") \
            + line_split[0].count("\t")*tabspaces

        self.depth = int((spaces - spaces % tabspaces) / tabspaces)
        if spaces % tabspaces:
            self.depth += 1

def real_lines(lines_from_config_file):
    r_lines = []
    for line in lines_from_config_file:
            # Ignore comments from the line
        val_line = line.split("#")[0]

            # check if the value is empty
        if val_line.replace(" ","") in ["", "\n"]:
            continue
        else:
            r_lines.append(
                Line(val_line)
            )
    return r_lines

def init_exercises_dir(
            exercises_dir_name = exercises_dir_name,
            forced = False
        ):
        # look for the configuration file
    exist, tree_files = find_tree_files_config()
    if not exist:
        print("[Error] Configuration file not found")
        return

        # read the lines of the config file
        # and clean them
    re_lines = real_lines(
        read_tree_files_config(tree_files)
    )
    
        # make exercises directory and move into it
    make_exercises_dir(forced, exercises_dir_name)
    os.chdir(exercises_dir_name)

        # from the project directory
        # starting from a depth 0
    prj_tree = []
    depth = 0
    
        # Archivo que incluye todo el árbol de archivos
    tree_tex = open("tree.tex", "w")
    tree_tex.write("% árbol de archivos\n\n")

        # init the directory
        # depending on the re_lines rules
    for line in re_lines:
            # new directory
        if line.flag == flags["dir"]:
                # checking if the depth is correct
            if depth == line.depth:
                prj_tree.append(line.parameter_files)
                depth += 1
            elif depth < line.depth:
                print("Invalid syntax in", tree_files, 'file')
                print("error in:", line.flag + line.parameter_files)
                sys.exit()
            else:
                splits = depth - line.depth
                for _ in range(splits):
                    prj_tree.pop()
                    depth -= 1
                prj_tree.append(line.parameter_files)

        directory = os.path.join(
                ".", "/".join(prj_tree)
            )
        if not os.path.isdir(directory):
            os.mkdir(directory)
            print((depth-1) * "\t" + "mkdir", prj_tree[-1])
            tree_tex.write(
                (depth-1) * "\t"
                + "\\section*{" 
                + prj_tree[-1] 
                + "}\n"
            )
            # new generic file
        if line.flag == flags["file"]:
            for file_name in line.parameter_files.split(" "):
                open(
                    os.path.join(
                        directory,
                        file_name
                    ),
                    'a'
                ).close()
                print(depth * "\t" + "touch", file_name)
                if file_name[-4:] == ".tex":
                    tree_tex.write(
                        depth * "\n"
                        + "\\input{ejercicios/"
                        + file_name[:-4]
                        + "}\n"
                    )
            # new LaTeX file
        if line.flag == flags["tex_file"]:
            for element in line.parameter_files.split(" "):
                shutil.copyfile(
                        custom_dirs.ej_tex,
                        os.path.join(
                            directory,
                            tex[0] + element + "." + tex[1]
                        )
                    )
                print(
                    depth * "\t" + "init", 
                    tex[0] + element + "." + tex[1]
                )
                tree_tex.write(
                    depth * "\t" 
                    + "\\input{ejercicios"
                    + directory[1:] + "/"
                    + tex[0] + element + "}\n"
                )
    tree_tex.close()
