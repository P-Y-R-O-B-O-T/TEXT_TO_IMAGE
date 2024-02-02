import os
import sys

#$$$$$$$$$$#

def CHEK_ARGS() :
    if len(sys.argv) != 3 :
        exit(0)

def CREATE_METADATA() :
    global COLOR_INDEX

def LOAD_SRC() :
    global FILE_DATA
    if "-b" == sys.argv[2] :
        FILE_DATA = open(sys.argv[1], "rb").readlines()
    elif "-n":
        FILE_DATA = open(sys.argv[1], "r").readlines()


def CREATE_MATRIX() :
    global COLOR_CODE
    global FILE_DATA

    max_len = max([len(_) for _ in FILE_DATA])

    COLOR_CODE = []
    for _ in range(len(FILE_DATA)) :
        COLOR_CODE.append([])
        for _ in range(max_len) :
            COLOR_CODE[-1].append(0)

    if "-b" == sys.argv[2] :
        for _ in range(len(FILE_DATA)) :
            for __ in range(len(FILE_DATA[_])) :
                COLOR_CODE[_][__] = (FILE_DATA[_][__])
    if "-n" == sys.argv[2] :
        for _ in range(len(FILE_DATA)) :
            for __ in range(len(FILE_DATA[_])) :
                COLOR_CODE[_][__] = ord(FILE_DATA[_][__])

    for _ in range(len(COLOR_CODE)) :
        if len(COLOR_CODE[_]) % 3 != 0 :
            #for _ in range(3 - (len(COLOR_CODE[_]) % 3)) :
            #    COLOR_CODE[_].append(0)
            if len(COLOR_CODE[_]) % 3 == 1 :
                COLOR_CODE[_].append(0)
                COLOR_CODE[_].append(0)
            if len(COLOR_CODE[_]) % 3 == 2 :
                COLOR_CODE[_].append(0)

def WRITE_TO_FILE() :
    global COLOR_CODE

    print("P3\n{0} {1}\n255\n".format(len(COLOR_CODE[0])//3, len(COLOR_CODE)))
    print("#", len(COLOR_CODE), len(COLOR_CODE[0]))

    for _ in range(0, len(COLOR_CODE)) :
        for __ in range(0, len(COLOR_CODE[_]), 1) :#3) :
            print(COLOR_CODE[_][__])
            """
            if __ + 3 <= len(COLOR_CODE[_]) - 1 :
                print("{0} {1} {2}\n".format(COLOR_CODE[_][__ + 0], COLOR_CODE[_][__ + 1], COLOR_CODE[_][__ + 2]))
            if __ + 2 == len(COLOR_CODE[_]) - 1 :
                print("{0} {1} {2}\n".format(COLOR_CODE[_][__ + 0], COLOR_CODE[_][__ + 1], 0))
            if __ + 1 == len(COLOR_CODE[_]) - 1 :
                print("{0} {1} {2}\n".format(COLOR_CODE[_][__ + 0], 0, 0))
            """

#$$$$$$$$$$#

if __name__ == "__main__" :
    CHEK_ARGS()
    CREATE_METADATA()
    LOAD_SRC()
    CREATE_MATRIX()
    WRITE_TO_FILE()
