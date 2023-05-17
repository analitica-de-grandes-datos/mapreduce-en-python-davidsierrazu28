#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
if __name__ == "__main__":
    suma_letra = {}
    contar_letra ={}
    
    for line in sys.stdin:
        columnas = line.split("\t")
        letra = columnas[0]
        valor = int(columnas[1])
        if letra in suma_letra:
            suma_letra[letra] += int(valor)
            contar_letra[letra] += 1
        else:
            suma_letra[letra] = int(valor)   
            contar_letra[letra] = 1
    
    for letra in sorted(suma_letra.keys()):
        promedio = suma_letra[letra] / contar_letra[letra]
        sys.stdout.write(f"{letra}\t{float(suma_letra[letra])}\t{promedio}\n")