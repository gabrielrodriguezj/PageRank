import numpy as np
import csv
import math


def csvAMatriz(archivoCSV):
    '''
    Este metodo recibe el archivo en formato csv, lo recorre, y convierte el texto a una matriz de 1 y 0.
     El 1 indica que existe una conexion entre los nodos (páginas web) que corresponden a la fila y columna donde aparece el valor 1
     El 0 indica que no existe un vínculo o relación.
     Es importante entender que la página que se representa en la columna i contienen enlaces o vínculos a las paginas dadas por las filas j (donde aparece el 1)

    :param archivoCSV:
    :return (matriz que contiene las conexiones entre los nodos o páginas):
    '''
    matriz = np.array([])
    i = 0
    for filaCSV in archivoCSV:
        i += 1

        if i == 1:
            #Fila que contiene las cabeceras de las columnas
            pass
        else:
            j = 0
            fila = []
            for celdaCSV in filaCSV:
                j += 1
                if j == 1:
                    #Columna 1, que contiene las cabeceras de las filas
                    pass
                else:
                    if celdaCSV == "1":
                        fila.append(1)
                    elif celdaCSV == "0":
                        fila.append(0)
            matriz = np.append([matriz], [fila])
    return np.matrix(matriz).reshape((i-1, i-1))

def MatrizTransicionesAMatrizProbabilidades(matrizVinculos):
    '''
    Este métdodo convierte la matriz de vínculos en una matriz de probabilidades.
     Esto se consigue sumando los vínculos que la pagina i contiene, es decir sumar la i-esima columna. Y después
     dividir cada elemento de dicha columna entre el total de vínculos.

    :param matrizVinculos:
    :return matrizProbabilidades:
    '''
    matrizProbabilidades = matrizVinculos.copy()
    for i in range(matrizVinculos.shape[0]):
        totalConexiones = sum(matrizVinculos[:, i]) #totalConexiones es una np.matrix, de la siguiente manera: [[ 1]].
        matrizProbabilidades[:, i] = (matrizVinculos[:, i] / totalConexiones) #No es necesario acceder al único elemento de totalConexiones con la siguiente forma totalConexiones[0, 0]
    return matrizProbabilidades

def MatrizDeTeletransportacion(n):
    '''
    Genera la matriz de teletransportación, es decir la probabilidad de poder transitar de una página a otra(o incluso quedarse en una página).
    :param n:
    :return:
    '''
    matrizTeletransportacion = np.matrix( [ [1/n]*n ]*n)
    return matrizTeletransportacion

def PowerMethod(matriz, diferencia):
    n = matriz.shape[0]
    x = np.array([1]*n)

    x = x[None, :]
    xAnterior = x.copy()

    dif = 1

    #print(matriz)
    #print(x)

    while dif > diferencia:
        #x = np.matmul(matriz, x)
        #x = np.multiply(matriz*x.transpose())

        x = matriz*x.transpose()



        norma = np.linalg.norm(x)
        x = x/norma

        error = x - xAnterior
        error = np.dot(error, error.transpose())
        error = np.sqrt(error)
        #error = math.sqrt(error)

        xAnterior = x.copy()


    return x


def main():
    archivo = open("Grafo1.csv","r")
    textoCSV = csv.reader(archivo, delimiter=',', skipinitialspace=False, strict=True)
    matrizVinculos = csvAMatriz(textoCSV)

    #Convertir matriz de los vínculos a matriz de probabilidades
    matrizProbabilidades = MatrizTransicionesAMatrizProbabilidades(matrizVinculos)

    matrizTeletransportacion = MatrizDeTeletransportacion(matrizVinculos.shape[0])

    d = 0.85

    matrizTransicion = d*matrizProbabilidades + (1-d)*matrizTeletransportacion

    eigenVector = PowerMethod(matrizTransicion, 0.0001)

    print(eigenVector)





if __name__ == "__main__":
    main()


'''
#Estas líneas de código pueden servir para cargar el csv si no tuviera cabeceras
archivoDatos = np.loadtxt("Grafo1.csv")
print(archivoDatos)

'''

'''
el algoritmo de PageRank funciona bajo la siguiente idea:
Se define una cadena de Markov que describe el comportamiento de la navegación por las páginas de internet.
Se calcula la matriz de probablidades-transicion, la cual contiene la probabilidad de que al visitar cierta página web, navegue hacia otra página a través de los vinculos que contiene la página actual
Se genera una matriz de teletransportación, que contiene las mismas dimensiones que la matriz de transiciones, pero todos los elementos son igual a 1/numero de páginas de internet. 
    Esta matriz representa la posibilidad que "tiene un usuario" de saltar de una página a otra. Esto va ayudar a que el método de potencias converja.
Se genera una matriz de transiciones que es igual a d*(Matriz de probabilidades) + (1-d)*(Matriz de teletransportacion). Donde d=0.85, el factor de amortizacion.
Se calcula el eigenvector de la matriz de transiciones con el metodo de potencias. El vector que resulte contendrá las ponderaciones 
    asignadas a las páginas web, entre más alto sea este valor, significa que la página tiene una mayor relevancia.
'''
