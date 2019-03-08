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
    #Se lee el archivo y se convierte a forma matricial
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

    '''
    #Estas líneas de código pueden servir para cargar el csv si no tuviera cabeceras
    archivoDatos = np.loadtxt("Grafo1.csv")
    print(archivoDatos)

    '''

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
    '''
    Metodo de potencias que calcula el eigenVector asociado al eigenvalor más grande.
    :param matriz:
    :param diferencia:
    :return:
    '''
    n = matriz.shape[0]
    x = np.array([1]*n)

    x = x[: , None]
    xAnterior = x.copy()

    dif = 1
    while dif > diferencia:
        x = np.matmul(matriz, x)
        #x = np.multiply(matriz*x.transpose())
        #x = matriz*x.transpose()

        norma = np.linalg.norm(x)
        x = x/norma

        error = x - xAnterior

        error = np.dot(error.transpose(), error)

        error = np.sqrt(error)
        #error = math.sqrt(error)

        xAnterior = x.copy()

        dif = error

    return x


def main():
    #Se abre el archivo csv con el titulo de cada página web
    archivo = open("grafo.csv","r")
    textoCSV = csv.reader(archivo, delimiter=',', skipinitialspace=False, strict=True)
    matrizVinculos = csvAMatriz(textoCSV)

    #Convertir matriz de los vínculos a matriz de probabilidades
    matrizProbabilidades = MatrizTransicionesAMatrizProbabilidades(matrizVinculos)

    #Genera la matriz de teletransportación
    matrizTeletransportacion = MatrizDeTeletransportacion(matrizVinculos.shape[0])

    #Factor de amortización.
    d = 0.85

    #Matriz de transición que representa al conjunto de páginas web
    matrizTransicion = d*matrizProbabilidades + (1-d)*matrizTeletransportacion

    #Se aplica el método de potencias para extraer el eigenVector de la matriz de transición
    #El eigenVector representa la importancia(relevancia) que tiene cada página web.
    eigenVector = PowerMethod(matrizTransicion, 0.0001)

    #Se despliegan los resultados obtenidos, se conserva el mismo orden establecido en el archivo csv.
    #eigenVector es una matriz. Para poder manipular y desplegar mejor los resultados
    #se convierte a lista (previamente se transpone para convertir el vector columa
    #a fila y sea más fácil manipular la lista)
    eigenVectorLista = eigenVector.transpose().tolist()[0]
    suma = sum(eigenVectorLista)
    rank = [(i/suma)*100 for i in eigenVectorLista]
    print(rank)


if __name__ == "__main__":
    main()
