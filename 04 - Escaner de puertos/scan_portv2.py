"""
Nombre: Johan Emmanuel Garay Garza
Matricula: 2001776
"""
import socket
def scan(addr, port):
    #Creando un nuevo socket
    socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #Estableciendo el timeout para el nuevo objeto tipo socket 
    socket.setdefaulttimeout (1)
    #Conexion exitosa devuelve 0. Devuelve error en caso contrario 
    result = socket_obj.connect_ex ((addr, port)) #Direccion y puerto en tupla.
    #Se cierra el objeto 
    socket_obj.close()
    return result
ports =[21, 22, 25, 80]
for i in range (1,255):
    addr="192.168.0.{}".format(i) 
    for port in ports:
        result= scan (addr, port) 
        if result==0:
            print (addr, port, "OK") 
        else:
            print (addr, port, "Failed")
