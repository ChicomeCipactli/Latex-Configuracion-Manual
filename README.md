# t-scripts

T-scripts automatiza tus tareas escritas en [LaTeX](https://en.wikipedia.org/wiki/LaTeX) además de ayudarte a mantener la configuración de tus tareas consistente.

## Dependencias

Para el correcto funcionamiento de estos scripts debes tener instalados 

- [Make](https://www.gnu.org/software/make/)
- [Python](https://www.python.org/)

## Instalación

### Linux

Dirígete a la carpeta `$HOME` de tu usuario de linux (simplemente ejecutando `cd`) y clona el repositorio con 
```
git clone https://github.com/ChicomeCipactli/Latex-Configuracion-Manual.git
```
Después desplázate hacia dicho repositorio (`cd $HOME/Latex-Configuracion-Manual`)
y ejecuta el script de instalación `./install.sh`.


El script de instalación escribirá al final de tu `.bashrc` y de tu `.zshrc` (si usas [zsh](https://wiki.archlinux.org/title/zsh))
la siguiente línea
```
export PATH=~/Latex-Configuracion-Manual/Scripts/:$PATH
```
Esto hará que los scripts de [bash](https::/wiki.archlinux.org/title/bash) de la carpeta `$HOME/Latex-Configuracion-Manual/Scripts/` sean reconocidos por tu sistema.
Podrás ejecutarlos dondequiera que estés.

## Configuración

Dirígete a la carpeta `$HOME/Latex-Configuracion-Manual/Ejemplos`. 
Ahí hay 3 ejemplos de proyectos `analisis-matematico-I`, `topologia-I`, `ecuaciones-diferenciales-parciales-I` y `metodos-numericos`.
Cada uno es una plantilla de un proyecto de [LaTeX](https://en.wikipedia.org/wiki/LaTeX) útil para mis tareas de la escuela.
La configuración de dichos proyectos depende de cómo quiero que funcionen mis tareas, pero puedes modificar sus nombres y toda 
la configuración para que se adapte a tu forma de trabajar, siempre y cuando no elimines el archivo `makefile` y seas cuidadoso con el archivo `tree.files`.

En la sección [Uso](#Uso) verás cómo generar el árbol de ejercicios. Por defecto cada ejercicio tiene nombre `ej<+>.tex` 
pero estoy trabajando para que puedas modificarlo
cada vez que comiences un nuevo proyecto con el proceso que se describe en dicha sección.

