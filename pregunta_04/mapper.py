#
# >>> Escriba el codigo del mapper a partir de este punto <<<
import sys
#from datetime import datetime

if __name__ == "__main__":
    for line in sys.stdin:
        #print (line)
        #print ("---")
        word = line.split(' ')
        #print (word[0])
        #print (word[3])
        #date = datetime.fromisoformat(word[3])
        #print (word[6].strip())
        sys.stdout.write("{},1\n".format(word[0]))
