#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
#from datetime import datetime

if __name__ == "__main__":
    for line in sys.stdin:
        #print (line)
        #print ("---")
        word = line.split(' ')

        sys.stdout.write("{},1\n".format(word[3].split('-')[1]))