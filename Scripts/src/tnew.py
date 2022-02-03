#!/usr/bin/python

import os 
import sys
import shutil
import readline

# source code

import routes
from completer import Completer
from readExampleConfig import reader

def defoult_templates():
    templates_names = os.listdir(
        routes.ejemplos_dir
    )

    # only showing the templates not the hidden files
    for t in templates_names:
        if t[0] == ".":
            templates_names.remove(t)

    return templates_names

def cli_ask_user():
    def_templates = defoult_templates()
    
    # setting the completer guide
    completer = Completer(ejemplos)
    readline.set_completer(completer.complete)
    readline.parse_and_bind('tab: complete')

    print("Defoult Templates")
    print(
        '-', 
        '\n- '.join(def_templates),
        '\n'
    )

    # Prompt 
    template_selected = input("> ")
    if not template_selected in def_templates:
        print(template_selected, "is not in the list")
        sys.exit() 

    print("Name of new project")
    project_name = input("> ") 
    
    return template_selected, project_name

    # supposing you already have the template and the new project's name
def new_project_defoult_template(template, project_name):
        # defining the routes
    template_path = os.path.join(routes.ejemplos_dir, template)
    common_files_path = os.path.join(
        routes.ejemplos_dir, ".comun"
    )
    common_tex_path = os.path.join(
        common_files_path, "tex"
    )
    new_project_dir = os.path.join(
        routes.curr_dir, project_name
    )
        # copying the tex common files into the new project directory
    shutil.copytree(
        common_tex_path, new_project_dir
    )
        # avoid copying the configuration file for the script
    for file in os.listdir(template_path):
        if file.split(".")[-1] != "tscripts":
            shutil.copy(
                os.path.join(
                    template_path,
                    file
                ),
                os.path.join(
                    new_project_dir,
                    "lib"
                )
            )
        # reading configuration file for project
    r = reader(
        template_path, 
        project_name, 
        new_project_dir
    )
    print(new_project_dir)
        # changing the apropiate main.tex name 
    os.chdir(new_project_dir)
    print(os.getcwd())
    print(r.main)
    os.rename("main.tex", r.main)
