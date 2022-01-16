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

    for i, e in enumerate(ejemplos):
        if e[0] == ".":
            ejemplos.pop(i)

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

    print("No estás poniendo atención luser!")
    sys.exit()

# -------------- PROGRAMA -----------------

def main():
    print("\nBienvenido a T-scripts\n")

    ejemplo, nombre = pideEjemplo()

    ejemplo_dir = ejemplos_dir + "/" + ejemplo
    comun_dir = ejemplos_dir + "/.comun"
    ejemplo_tex_dir = comun_dir + "/" + "tex"

    new_dir = curr_dir + "/" + nombre

    shutil.copytree(ejemplo_tex_dir, new_dir)
    for f in os.listdir(ejemplo_dir):
        if f.split(".")[-1] != "tscripts":
            shutil.copy(
                ejemplo_dir + "/" + f, 
                new_dir + "/lib/" 
            )

    r = reader(ejemplo_dir, nombre, ejemplo)

    new_main_tex = r.main

    os.chdir(new_dir)
    os.rename("main.tex", new_main_tex)

if __name__ == '__main__':
    main()
