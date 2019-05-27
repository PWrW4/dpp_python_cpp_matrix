import ctypes as ct
import os


def main():
    matrix = ct.cdll.LoadLibrary("dpp_python_matrixLibCPP.dll")

    FLOAT = ct.c_float
    PFLOAT = ct.POINTER(FLOAT)
    INT = ct.c_int

    size = int(input("Podaj rozmiar macierzy: "))

    sizeToPass = INT(size)

    FLTTOARR = FLOAT * size
    PFLTTOARR = PFLOAT * size

    matrix.calc_power.argtypes = [PFLTTOARR,
                                  PFLTTOARR,
                                  INT]

    matrix.calc_power.restype = ct.POINTER(ct.POINTER(ct.c_float))

    ptrA = PFLTTOARR()
    ptrB = PFLTTOARR()

    for i in range(size):
        ptrA[i] = FLTTOARR()
        for j in range(size):
            ptrA[i][j] = int(input("Podaj dla A " + str(i) + str(j) + ": "))

    for i in range(size):
        ptrB[i] = FLTTOARR()
        for j in range(size):
            ptrB[i][j] = int(input("Podaj dla B " + str(i) + str(j) + ": "))

    ret = matrix.calc_power(ptrA, ptrB, sizeToPass)

    for i in range(size):
        for j in range(size):
            print("Wynik " + str(i) + str(j) + ": " + str(ret[i][j]))

    input()


if __name__ == "__main__":
    main()
