#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == "__main__":

    meses = {}
    for line in sys.stdin:
        key,val = line.split("\t")
        val = int(val)
        if key in meses:
            meses[key] += val
        else:
            meses[key] = val
    meses_ordenados= sorted(meses.items(),key=lambda x: x[0])
    for item in meses_ordenados:
        sys.stdout.write(f"{item[0]}\t{item[1]}\n")
    