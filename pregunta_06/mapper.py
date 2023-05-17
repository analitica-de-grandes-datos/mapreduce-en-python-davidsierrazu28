#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "__main__":
    for line in sys.stdin:
        columnas = line.split(" ")
        columna1 = columnas[0]
        columna2 = float(columnas[6])
        sys.stdout.write(f"{columna1}\t{columna2}\n")