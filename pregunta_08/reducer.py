#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
# ! /usr/bin python3
import sys

if __name__ == '__main__':

    curkey = None
    totalv = 0
    totalc = 0
    for line in sys.stdin:

        key, val, count = line.split("   ")
        val = float(val)
        count = float(count)
        # print (key)

        if key == curkey:
            totalv += val
            totalc += count

        else:
            if curkey is not None:
                a = totalv / totalc
                # print(a)
                # print(totalc)
                sys.stdout.write("{}\t{}\t{}\n".format(curkey, totalv, a))
            curkey = key
            totalv = val
            totalc = count
            # a =totalv/totalc
            # print(a)
            # print(totalc)
            # print('none')

    a = totalv / totalc
    sys.stdout.write("{}\t{}\t{}\n".format(curkey, totalv, a))