# Latex-Configuracion-Manual

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
Esto hará que los scripts de [bash](https::/wiki.archlinux.org/title/bash) de la carpesta `$HOME/Latex-Configuracion-Manual/Scripts/` sean reconocidos por tu sistema.
De esta manera podrás ejecutarlos dondequiera que estés.
