import os
import sys

#$$$$$$$$$$#
# qweqwe :dfsdfs
def CHEK_ARGS() :
    if len(sys.argv) != 3 :
        exit(0)

def CREATE_METADATA() :
    global COLOR_INDEX

def LOAD_SRC() :
    global FILE_DATA
    if "-b" == sys.argv[2] :
        FILE_DATA = open(sys.argv[1], "rb").read()
    elif "-n":
        FILE_DATA = open(sys.argv[1], "r").read()


def CREATE_MATRIX() :
    global COLOR_CODE
    COLOR_CODE = []
    max_index = len(FILE_DATA) - 1
    for _ in range(0, len(FILE_DATA), 3) :
        if (_ + 3) <= max_index :
            if "-b" == sys.argv[2] :
                COLOR_CODE.append([(FILE_DATA[_+__])
                                   for __ in range(3)])
            else :
                COLOR_CODE.append([ord(FILE_DATA[_+__])
                                   for __ in range(3)])
        elif (_ + 2) == max_index :
            if "-b" == sys.argv[2] :
                COLOR_CODE.append([(FILE_DATA[_+__])
                                   for __ in range(2)] + [0])
            else :
                COLOR_CODE.append([ord(FILE_DATA[_+__])
                                   for __ in range(2)] + [0])
        elif (_ + 1) == max_index :
            if "-b" == sys.argv[2] :
                COLOR_CODE.append([(FILE_DATA[_+__])
                                   for __ in range(1)] + [0, 0])
            else :
                COLOR_CODE.append([ord(FILE_DATA[_+__])
                                   for __ in range(1)] + [0, 0])

def WRITE_TO_FILE() :
    global COLOR_CODE

    grid_width = 0
    while grid_width*grid_width < len(COLOR_CODE) :
        grid_width += 1

    print("P3\n{0}\n{0}\n255".format(grid_width))

    for _ in COLOR_CODE :
        print("{0} {1} {2}\n".format(_[0], _[1], _[2]))

#$$$$$$$$$$#

if __name__ == "__main__" :
    CHEK_ARGS()
    CREATE_METADATA()
    LOAD_SRC()
    CREATE_MATRIX()
    WRITE_TO_FILE()
