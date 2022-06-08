#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
#from datetime import datetime
#print(sys.stdin.readlines()[0].split('   ')[2].strip())
maxi = 3
if __name__ == "__main__":
    for line in sys.stdin:
        sys.stdout.write("{}   {}   1\n".format(str(line.split('   ')[0]), line.split('   ')[2].strip()))