'''
Contiene todas las operaciones de algebra lineal que se requieren para el PageRank.
'''
import math

def EscalarPorMatriz(escalar, matriz):
    '''
    Esta función multiplica cualquier matriz por un escalar.
    '''
    n = len(matriz)
    return [[matriz[x][y]*escalar for x in range(n)] for y in range(n)]

def SumaMatrices(matriz1, matriz2):
    '''
    Esta función suma dos matrices; Se espera que matriz1 y matriz2 sean del mismo tamaño.
    '''
    n = len(matriz1)
    return [[matriz1[i][j]+matriz2[i][j] for j in range(n)] for i in range(n)]


def PowerMethod(matriz, diferencia):
    '''
    Metodo de potencias que calcula el eigenVector asociado al eigenvalor más grande.
    '''
    n = len(matriz)
    x = [1]*n
    xAnterior = x.copy()

    dif = 1

    while dif > diferencia:
        x = MultiplicacionMatrizVector(matriz, x)

        x = NormalizarVector(x)

        error = DiferenciaVectores(x, xAnterior)
        error = ProductoPunto(error, error)
        error = math.sqrt(error)
        xAnterior = x.copy()

        dif = error

    return x

def MultiplicacionMatrizVector(matriz, vector):
    '''
    Este método realiza la multiplicación de una matriz por un vecor (no al revés).
    '''
    x = vector.copy()
    i = 0
    for vec in matriz:
        x[i]  = ProductoPunto(vec, vector)
        i = i + 1
    return x

def ProductoPunto(vector1, vector2):
    '''
    Este método realiza la multiplicación de un vector por otro vector.
    '''
    producto = 0
    for i in range(len(vector1)):
        producto = producto + vector1[i] * vector1[i]
    return producto

def NormalizarVector(vector):
    '''
    Este método calcula la norma de un vector, y divide cada elemento entre la norma.
    '''
    sumaCuadrados = sum([x*x for x in vector])
    norma = math.sqrt(sumaCuadrados)

    return [x/norma for x in vector]

def DiferenciaVectores(vector1, vector2):
    '''
    Este método resta dos vectores.
    '''
    return [vector1[i] - vector2[i] for i in range(len(vector1))]
