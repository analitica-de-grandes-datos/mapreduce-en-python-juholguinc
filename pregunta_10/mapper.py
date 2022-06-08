#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
maxi = 2
if __name__ == "__main__":
    for line in sys.stdin:
        a, b = line.split('\t')
        b =list(b.strip().split(','))
        a = a.zfill(maxi)
        for x in b:
            sys.stdout.write("{}\t{}\n".format(x,a))
