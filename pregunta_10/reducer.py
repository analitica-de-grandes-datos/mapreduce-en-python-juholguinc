#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
# ! /usr/bin python3

import sys

if __name__ == '__main__':

    curkey = None
    total = 0

    for line in sys.stdin:

        key, val = line.split("\t")
        val = val.strip()

        if key == curkey:
            #
            # No se ha cambiado de clave. Aca se acumulan los valores para la misma
            # clave.
            #
            cadena = cadena + ',' + str(int(val))
        else:
            #
            # Se cambio de clave. Se reinicia el acumulador.
            #
            if curkey is not None:
                #
                sys.stdout.write("{}\t{}\n".format(curkey, cadena))

            curkey = key
            cadena = str(int(val))

    sys.stdout.write("{}\t{}\n".format(curkey, cadena))