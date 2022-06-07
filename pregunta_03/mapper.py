#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "__main__":
    for line in sys.stdin:
        #print (line)
        #print ("---")
        word = line.split(',')
        #print (word[0])
        #print (word[1].strip())
        #print (word[0])
        sys.stdout.write("{},{}\n".format(word[1].strip(),word[0]))