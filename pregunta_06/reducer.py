#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
if __name__ == "__main__":
    maximos = {}
    minimos = {}
    for line in sys.stdin:
        columnas = line.strip().split("\t")
        letra = columnas[0]
        valor = float(columnas[1])
        if letra in maximos:
            maximos[letra] = max(maximos[letra],valor)
        else:
            maximos[letra] = valor
        if letra in minimos:
            minimos[letra] = min(minimos[letra],valor)
        else:
            minimos[letra] = valor
    for letra in sorted(maximos.keys()):
        sys.stdout.write(f"{letra}\t{maximos[letra]}\t{minimos[letra]}\n")
    
        
        
        
