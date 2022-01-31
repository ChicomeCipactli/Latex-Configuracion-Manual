import os

home_dir = os.path.expanduser("~")  # Equivalente a $HOME

T_dir = home_dir + '.config/tscripts'
ejemplos_dir = T_dir + '/Ejemplos'
scripts_dir = T_dir + '/Scripts'

curr_dir = os.getcwd() 
