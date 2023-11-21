#!/bin/bash
#
# Menú en BASH con opciones adicionales
#
date
echo "||"
echo "||===========================||"
echo "||   Menu Principal          ||"
echo "||===========================||"
echo "||I. Net Discover"
echo "||II. Port Scan v1"
echo "||III. Welcome"
echo "||IV. Exit"
echo "||"
read -p "Opción  [ 1 - 4 ] " c

case $c in
    1) $HOME/netdiscover.sh;;
    2) echo "Ejecutando portscanv1.sh"
       $HOME/portscanv1.sh;;
    3) echo "Ejecutando welcome.sh"
       $HOME/welcome.sh;;
    4) echo "Bye!"; exit 0;;
    *) echo "Opción no válida. Introduce un número del 1 al 4.";;
esac
