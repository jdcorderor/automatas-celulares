import time

cadena = input("Ingrese una cadena binaria (0s y 1s): ")
iteraciones = int(input("Ingrese el número de iteraciones: "))

cadena = cadena.replace("0"," ").replace("1","█")

# Diccionario con la "regla" del autómata "Regla 110".
regla = {"   ":" ","  █":"█"," █ ":"█"," ██":"█",
        "█  ":" ","█ █":"█","██ ":"█","███":" "}

for k in range(iteraciones):
    salida = ""

    # Ciclo del autómata "Regla 110", que recorre la cadena binaria.
    for i in range(len(cadena)):
        # En el caso del primer caracter...
        if i == 0:
            patron = " " + cadena[0] + cadena[1]

        # En el caso del último caracter...
        elif i == len(cadena) - 1:
            patron = cadena[-2] + cadena[-1] + " "

        # En el restante de casos...
        else:
            patron = cadena[i-1] + cadena[i] + cadena[i+1]
        salida += regla[patron]
    
    time.sleep(0.05)

    # Imprimir la salida de la iteración.
    print(salida)
    
    # Asignar a la variable "cadena" la salida de la iteración.
    cadena = salida 