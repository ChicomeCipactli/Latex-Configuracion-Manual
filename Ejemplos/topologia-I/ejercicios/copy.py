#!/usr/bin/python

import os 
import sys
from shutil import copyfile

dir_path = os.path.dirname( os.path.realpath( __file__ ) ) 
templeteFile = "t.tex"          # no cambies el nombre del archivo

flags = [
    "-S",    # The section name. Default: "sec"
    "-F",    # Filename. Default "ej"
    "-E",    # Extention. Default: "tex"
    "-sn",   # section number
    "-fn"    # file number
]

S = "sec"
F = "ej"
E = "tex"
sn = "0"
fn = "0"

def changeSec( argv = sys.argv ):
    argv = iter( argv )
    for arg in argv:
        if arg == "-S":
            S = next( argv )

def changeExt( argv = sys.argv ):
    argv = iter( argv )
    for arg in argv:
        if arg == "-E":
            E = next( argv )

def changeFil( argv = sys.argv ):
    argv = iter( argv )
    for arg in argv:
        if arg == "-F":
            F = next( argv )

def dirs( S = S, argv = sys.argv ):
    dirs = [ ]
    argv = iter( argv )
    for arg in argv:
        if arg == "-sn":
            dirs.append( S + next( argv ) )
        else:
            continue
    return dirs


def files( F = F, E = E, dirnum = 1, argv = sys.argv ):
    sections = 0
    files = [ ]
    argv = iter( argv )
    for arg in argv :
        if arg == "-sn":
            sections += 1
            next( argv )
            continue
        if arg == "-fn":
            continue
        if sections == dirnum:
            files.append( F + arg + "." + E )
        if sections > dirnum:
            break
    return files

changeFil( )
changeExt( )
changeSec( )

dirs = dirs( )
files = [ files( dirnum = i + 1 ) for i in range( len( dirs ) ) ]

if len( dirs ) != len( files ):
    exit( "Arguments were passed in a wrong way" )

for idx, d in enumerate( dirs ):
    if not os.path.exists( d ):
        os.mkdir( "./" + d )
        print( "mkdir {}".format( "./" + d ) )
        for f in files[ idx ]:
            if not os.path.exists( "./" + d + f ):
                copyfile( templeteFile, "./" + d + "/" + f )
                print( "touch {}".format( "./" + d + "/" + f ) )

