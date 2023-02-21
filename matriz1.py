import numpy
arreglo = numpy.array([[3,10,4,16],[1,7,8,-7],[9,-1,3,9]])
for i in range(3):
    for j in range(4):
        print(arreglo[i][j], end="")
        print("\t", end="")
    print("")
