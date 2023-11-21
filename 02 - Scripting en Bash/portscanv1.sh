#!/bin/bash
# Script number.sh
# 19/9/2023 - Johan Garay
# Escaner de puertos usando archivo especial en /dev
# Escrito en bash
#
# Definicion de variables
direccion_ip=$1
puertos="20,21,22,23,25,50,51,53,80,110,119,135,136,134,138,139,143,161,389,443,445,636,1025,1443,3389,5985,5986,8080,10000"
# Verificando que parametro ip no vengan vacio
[ $# -eq 0 ] && { echo "Modo de uso $0 <direccion ip>"; exit 1; }
#
# Bucle for para cada puerto en $puertos
#
IFS=,
for port in $puertos
do
	timeout 1 bash -c "echo > /dev/tcp/$direccion_ip/$port > /dev/null 2>&1" &&\
	echo $direccion_ip":"$port" is open"\
	||\
	echo $direccion_ip":"$port" is closed"
done
