# sys
import os

# matplotlib
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import collections as mc

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.serif": ["Palatino"],
})

# crear directorios [ Aviso: estoy suponiendo que estoy en una carpeta src/ dentro del proyecto
                    # donde yo generalmente tengo mis códigos ]
if not os.path.isdir( "../img" ):
    os.mkdir( "../img" )

path = [ 
    "../img/problema" + str( problema ) + "/" for problema in [ 2, 3, 5 ]
]

for p in path:
    if not os.path.isdir( p ):
        os.mkdir( p )

     # graphs es un vector de graficas que constan de dos listas: 
    #               una correspondiente a los datos del dominio y 
    #               la otra a los de la funcion
    # Por ejemplo:
    #     graphs = [ 
    #                 [ [ 0, 1 ], [ 0, 1 ] ], // Esta sera una grafica 
    #                 [ [ 0, 1 ], [ 1, 2 ] ], // y esta corresponde a otra 
    #                                        // que se grafica simultaneamente
    #             ]
def plot( 
            graphs, legends = [ ], 
            legends_loc = "best",
            tp = [ 'o', 'o', 'o', 'o' ],
            name = "fig.png", main = "Gráfica", 
            xlab = "Valores de $t$",
            ylab = "Valores de $y(t)$",
            path = "./",  
            colors = [ 'y', 'c', 'm', 'r', 'g', 'b', 'k' ],
            zoomX = 0,
            zoomY = 0
        ):
    fig, ax = plt.subplots( figsize = ( 6, 4 ), tight_layout = True )
    ax.set_title( r'{}'.format( main ), fontsize = 16 )

    for idx, graph in enumerate( graphs ):
        marker = 'o'
        if idx < len( tp ):
            marker = tp[ idx ]
        if idx >= len( legends ):
            ax.plot( 
                    graph[ 0 ],
                    graph[ 1 ],
                    marker,
                    # fmt = tp,
                    color = colors[ idx % len( colors ) ]
                )
        else:
            ax.plot( 
                    graph[ 0 ],
                    graph[ 1 ],
                    marker,
                    # fmt = tp,
                    color = colors[ idx % len( colors ) ],
                    label = r'{}'.format( legends[ idx ] )
                )
    if len( legends ) > 0:
        ax.legend( legends, loc = legends_loc )
    # ax.autoscale( )
    ax.margins( zoomX, zoomY )

    ax.set_xlabel( r'{}'.format( xlab ), fontsize = 14 )
    ax.set_ylabel( r'{}'.format( ylab ), fontsize = 14 )
    ax.grid( True )

    plt.savefig( name )
    os.replace( name, path + name )

import numpy as np

dominio = np.linspace( -1, 1, num = 100 )

ys1 = dominio ** 2
ys2 = dominii ** 3
plot( 
    graphs = [
            [ dominio, ys1 ],
            [ dominio, ys2 ]
        ],
    legends = [
            "$f(x)=x^2$",
            "$g(x)=x^3$"
        ],
    xlab = "Valores de x",
    ylab = "Imágenes",
    tp = [
        "-",
        "--"
    ],
    zoomX = 0.1,
    zoomY = 0.1
)
