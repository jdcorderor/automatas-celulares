import time

cadena = input("Ingrese una cadena (0 y 1): ")
iteraciones = int(input("Ingrese el número de iteraciones: "))
cadena = cadena.replace("0"," ").replace("1","█") # Reemplaza 0 por espacio y 1 por bloque lleno (█) para visualización

regla = {"   ":" ","  █":"█"," █ ":"█"," ██":"█",       # Regla 110 (Original)
        "█  ":" ","█ █":"█","██ ":"█","███":" "}

regla_triangulo = {"   ": " ", "  █": "█", " █ ": "█", " ██": " ", # reglas actualizadas
                    "█  ": "█", "█ █": " ", "██ ": "█", "███": " "}

print(cadena)                                   # imprime por consola la cadena inicial
for k in range(iteraciones):                    #Itera el número de veces que se ha indicado
    nueva_cadena = ""                           # crea una cadena vacia la cual se rellenará tomando en cuenta la última cadena y las reglas
    for i in range(len(cadena)):                # se recorre la cadena
        if i == 0:                              # en caso de ser el primer elemento, se rellena con 0 el elemento a la izquierda del pivote
            patron = " " + cadena[0] + cadena[1]
        elif i == len(cadena) - 1:              # en caso de ser el último elemento, se rellena con 0 el elemento a la derecha del pivote
            patron = cadena[-2] + cadena[-1] + " "
        else:                                   # se crea un patron tomando en cuenta el elemento a la izquierda, el elemento actual y el elemento a la derecha
            patron = cadena[i-1] + cadena[i] + cadena[i+1]
        nueva_cadena += regla_triangulo[patron]
    time.sleep(0.05)                            # retardo de 0.05 segundos para visualizar un efecto de aparición
    print(nueva_cadena)                         # imprime por consola la nueva cadena
    cadena = nueva_cadena                       # actualiza la cadena para la siguiente iteración