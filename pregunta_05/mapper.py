#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "__main__":
    fechas = []
    for line in sys.stdin:
        columnas = line.split(" ")
        columna_fecha= columnas[3]
        fechas.append(columna_fecha)
    
    for f in fechas:
        mes = f.split("-")[1]
        sys.stdout.write(f"{mes}\t1\n")
