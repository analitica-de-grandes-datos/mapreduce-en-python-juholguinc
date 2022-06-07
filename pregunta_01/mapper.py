#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "__main__":
    for line in sys.stdin:
        #print (line)
        #print (type(line))
        word = line.split(',')
        #print (word[2])
        sys.stdout.write("{}\t1\n".format(word[2]))