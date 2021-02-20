import matplotlib.pyplot as plt
import matplotlib as mpl
import math
import os

if not os.path.isdir( "../img" ):
    os.mkdir( "../img" )

if not os.path.isdir( "../img/ejercicio3" ):
    os.mkdir( "../img/ejercicio3" )

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
    # return ( t + 2 ( t ** 3 ) / 3 + ( t ** 5 ) / 5 + c ) * math.cos( math.atan( t ) )
    return math.cos( math.atan( t ) )

for c in range( -1, 2 ):
    x_axis = [ x / 20 for x in range( -2000,  2001 ) ]
    y_axis = [ ]
    for t in x_axis:
        y_axis.append( y( t, 5 * c ) )
    
    fig, ax = plt.subplots(figsize=(6, 4), tight_layout=True)
    ax.plot( x_axis, y_axis )

    ax.set_xlabel( r'Valores de $t$', fontsize = 14 )
    ax.set_ylabel( r'Valores de $y(t)$', fontsize = 14 )
    ax.set_title( r'Con parámetro $c_1 = ' + str( 5 * c ) +
                 r'$', fontsize=15 )

    # plt.plot( x_axis, y_axis )
    # plt.xlabel(r'\frac{2}{5}')

    # plt.show( )
    name = "fig" + str( 5 * c ) + ".png"
    print(name)
    plt.savefig( name )
    # plt.savefig(fname = "c(" + str( c ) + ").png", dpi=None, facecolor='w', edgecolor='w',
    #     orientation='portrait', papertype=None, format=None,
    #     transparent=False, bbox_inches=None, pad_inches=0.1,
    #     frameon=None, metadata=None)
    os.replace( name, "../img/ejercicio3/" + name )

    
