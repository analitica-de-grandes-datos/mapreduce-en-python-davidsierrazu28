#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
if __name__ == "__main__":
    suma_credito = {}
    for line in sys.stdin:
        columnas = line.split("\t")
        credito = columnas[0]
        valor = int(columnas[1])
        if credito in suma_credito:
            suma_credito[credito] = max(suma_credito[credito],valor)
        else:
            suma_credito[credito] = valor

    suma_credito_orden = sorted(suma_credito.items())
    for atributo,valor in suma_credito_orden:
        sys.stdout.write(f"{atributo}\t{valor}\n")


      