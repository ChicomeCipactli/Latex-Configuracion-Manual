#! /usr/bin/python

import os
import sys
import readline
import shutil

path_proyecto = '/home/juamnito/Latex-Configuracion-Manual'
path_ejemplos = path_proyecto + '/Ejemplos'

class Completer(object):

    def __init__(self, options):
        self.options = sorted(options)

    def complete(self, text, state):
        if state == 0:  # on first trigger, build possible matches
            if text:
                self.matches = [ s for s in self.options if s.startswith(text) ]
            else:
                self.matches = self.options[:]
        try:
            return self.matches[state]
        except IndexError:
            return None

ejemplos = os.listdir(path_ejemplos)

completer = Completer(ejemplos)
readline.set_completer(completer.complete)
readline.parse_and_bind('tab: complete')

def pideEjemplo():
    print("¿Cuál ejemplo de proyecto quieres copiar?")
    print(' '.join(ejemplos))
    
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
currdir = os.getcwd()

shutil.copytree(path_ejemplos + "/" + ejemplo, currdir + "/" + nombre)

os.chdir(currdir + "/" + nombre)
os.rename("main.tex", ejemplo + "-" + nombre + "-Juan_Parra.tex")
