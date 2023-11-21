import nmap

def escaneo_udp(target):
    nm = nmap.PortScanner()
    nm.scan(target, arguments='-p U:1-1000')
    print("Resultados del escaneo UDP:")
    print(nm.all_hosts())
    print(nm[target].all_protocols())
    print(nm[target]['udp'].keys())

def escaneo_completo(target):
    nm = nmap.PortScanner()
    nm.scan(target, arguments='-p 1-65535 -sS -sV -O -A')
    print("Resultados del escaneo completo:")
    print(nm.all_hosts())
    print(nm.csv())

def deteccion_sistema_operativo(target):
    nm = nmap.PortScanner()
    nm.scan(target, arguments='-O')
    print("Deteccion de sistema operativo:")
    print(nm[target]['osclass'])

def escaneo_con_ping(target):
    nm = nmap.PortScanner()
    nm.scan(target, arguments='-sn')
    print("Resultados del escaneo de red con ping:")
    print(nm.all_hosts())

def menu():
    while True:
        print("\nMeno de opciones:")
        print("1. Escaneo UDP")
        print("2. Escaneo Completo")
        print("3. Deteccion de sistema operativo")
        print("4. Escaneo de red con ping")
        print("5. Salir")

        opcion = input("Ingrese el numero de la opcion deseada: ")

        if opcion == '1':
            target = input("Ingrese la direccion IP del objetivo: ")
            escaneo_udp(target)
        elif opcion == '2':
            target = input("Ingrese la direccion IP del objetivo: ")
            escaneo_completo(target)
        elif opcion == '3':
            target = input("Ingrese la direccion IP del objetivo: ")
            deteccion_sistema_operativo(target)
        elif opcion == '4':
            target = input("Ingrese la direccion de red para el escaneo con ping (ej. 192.168.1.0/24): ")
            escaneo_con_ping(target)
        elif opcion == '5':
            break
        else:
            print("Opcion no valida. Por favor, elija una opcion valida.")

if __name__ == "__main__":
    menu()
