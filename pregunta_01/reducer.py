#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
if __name__ == "__main__":
    atributo = {}
    for line in sys.stdin:
        columnas = line.split("\n")
        columna1 = columnas[0]
        if columna1 in atributo:
            atributo[columna1] += 1
        else:
            atributo[columna1] =1
    atributo_orden = sorted(atributo.items())
    for atributo,valor in atributo_orden:
        sys.stdout.write(f"{atributo}\t{valor}\n")
    