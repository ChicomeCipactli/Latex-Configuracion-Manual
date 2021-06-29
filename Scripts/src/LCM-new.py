#! /usr/bin/python

import os
import sys
import readline
import shutil

# ---- Propios ----

from routes import *
from completer import Completer
from readExampleConfig import reader

def pideEjemplo():
    ejemplos = os.listdir(ejemplos_dir)

    completer = Completer(ejemplos)
    readline.set_completer(completer.complete)
    readline.parse_and_bind('tab: complete')

    print("¿Cuál ejemplo de proyecto quieres copiar?\n")
    print('-', '\n- '.join(ejemplos), '\n')

    for _ in range(3):
        ejemplo = input("> ")

        if ejemplo in ejemplos:

            print("¿Con qué nombre?")
            nombre = input("> ")

            return ejemplo, nombre
        else:
            print("Ese no está en la lista")

    print("No estás poniendo atención. ¡Despierta!")
    sys.exit()

# -------------- PROGRAMA -----------------

print("\nBienvenido a Latex-Configuracion-Manual\n")

ejemplo, nombre = pideEjemplo()

ejemplo_dir = ejemplos_dir + "/" + ejemplo
ejemplo_tex_dir = ejemplo_dir + "/" + "tex"

new_dir = curr_dir + "/" + nombre
shutil.copytree(ejemplo_tex_dir, new_dir)

r = reader(ejemplo_dir, nombre, ejemplo)

new_main_tex = r.main

os.chdir(new_dir)
os.rename("main.tex", new_main_tex)
