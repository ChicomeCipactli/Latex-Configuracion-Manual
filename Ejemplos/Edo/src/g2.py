import matplotlib.pyplot as plt
import matplotlib as mpl
import math
import os

if not os.path.isdir( "../img" ):
    os.mkdir( "../img" )

if not os.path.isdir( "../img/ejercicio2" ):
    os.mkdir( "../img/ejercicio2" )

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "sans-serif",
    "font.sans-serif": ["Times New Roman"]
})
## for Palatino and other serif fonts use:
# plt.rcParams.update({
#     "text.usetex": True,
#     "font.family": "serif",
#     "font.serif": ["Palatino"],
# })

def y( t, c ):
    return - math.log( - math.exp( t + 3 ) + c )

for p in range( 1, 4 ):
    c = p / 3
    x_axis = [ x / 20 for x in range( -50,  51 ) ]
    y_axis = [ ]
    for t in x_axis:
        if t < math.log(c)-3:
            print( y(t,0) )

            y_axis.append( y( t, 0 ) )
        else:
            y_axis.append(0)

    fig, ax = plt.subplots(figsize=(6, 4), tight_layout=True)
    ax.plot( x_axis, y_axis )

    ax.set_xlabel( r'Valores de $t$', fontsize = 14 )
    ax.set_ylabel( r'Valores de $y(t)$', fontsize = 14 )
    ax.set_title( r'Parámetro $c=' +str(c) +r'$', fontsize=15 )

    # plt.plot( x_axis, y_axis )
    # plt.xlabel(r'\frac{2}{5}')

    plt.show( )
    # name = "fig" + str(c) + ".png"
    # plt.savefig( name )
    # # plt.savefig(fname = "c(" + str( c ) + ").png", dpi=None, facecolor='w', edgecolor='w',
    # #     orientation='portrait', papertype=None, format=None,
    # #     transparent=False, bbox_inches=None, pad_inches=0.1,
    # #     frameon=None, metadata=None)
    # os.replace( name, "../img/ejercicio2/" + name )
