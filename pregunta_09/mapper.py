#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
#from datetime import datetime
#print(sys.stdin.readlines()[0].split('   ')[2].strip())
maxi = 3
if __name__ == "__main__":
    for line in sys.stdin:
        strnum = line.split('   ')[2].strip()
        strnum = strnum.zfill(maxi)
        sys.stdout.write("{}   {}   {}\n".format(strnum, line.split('   ')[0] , line.split('   ')[1]))