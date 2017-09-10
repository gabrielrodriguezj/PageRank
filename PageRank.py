import csv
import copy
from linealalgebra import *

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
    matrizCaracteres = [x for x in [y for y in archivoCSV]]
    n = len(matrizCaracteres)

    #Se eliminan las etiquetas de las columnas
    matrizCaracteresSinCabecerasColumnas = [matrizCaracteres[x] for x in range(1,n)]
    #Se eliminan las etiquetas de las filas
    matriz = [[int(matrizCaracteresSinCabecerasColumnas[y][x]) for x in range(1,n)] for y in range(n-1)]

    return matriz

    '''
    #Estas líneas de código pueden servir para cargar el csv si no tuviera cabeceras
    archivoDatos = np.loadtxt("Grafo1.csv")
    print(archivoDatos)

    '''

def MatrizVinculosAMatrizProbabilidades(matrizVinculos):
    '''
    Este métdodo convierte la matriz de vínculos en una matriz de probabilidades.
     Esto se consigue sumando los vínculos que la pagina i contiene, es decir sumar la i-esima columna. Y después
     dividir cada elemento de dicha columna entre el total de vínculos.

    :param matrizVinculos:
    :return matrizProbabilidades:
    '''
    matrizProbabilidades = matrizVinculos.copy()
    n = len (matrizProbabilidades);

    #Se transpone matrizProbabilidades (copia de matrizVinculos) para que sea sencillo el sumar cada columna de la matrizProbabilidades.
    matrizProbabilidadesTranspuesta = [[fila[i] for fila in matrizProbabilidades] for i in range(n)]
    #Se suma cada fila de matrizProbabilidadesTranspuesta para determinar el total de vinculos que tiene cada página.
    totalConexiones = [sum(x) for x in matrizProbabilidadesTranspuesta]

    #Se divide cada elemento de cada columna, entre el número de conexiones representadas en cada columna
    matrizProbabilidades  =  [[matrizProbabilidades[i][j]/ totalConexiones[j] for j in range(n) ] for i in range(n) ]
    '''
    for i in range(n):
        for j in range (n):
            matrizProbabilidades[i][j] = matrizProbabilidades[i][j] / totalConexiones[j]
    '''

    return matrizProbabilidades

def MatrizDeTeletransportacion(n):
    '''
    Genera la matriz de teletransportación, es decir la probabilidad de poder transitar de una página a otra(o incluso quedarse en una página).
    :param n:
    :return:
    '''
    matrizTeletransportacion = [[1/n]*n]*n
    return matrizTeletransportacion

def MatrizDeTransicion(d, matrizProbabilidades, matrizTeletransportacion):
    '''
    Genera la matriz de transicion, bajo la siguiente regla
    matrizTransicion = d*matrizProbabilidades + (1-d)*matrizTeletransportacion
    :param n:
    :return:
    '''
    m1 = EscalarPorMatriz(d,matrizProbabilidades)
    m2 = EscalarPorMatriz(1-d,matrizTeletransportacion)

    matrizTransicion = SumaMatrices(m1, m2)

    return matrizTransicion


def main():
    #Se abre el archivo csv con el titulo de cada página web
    archivo = open("Ejemplos\Grafo1.csv","r")
    textoCSV = csv.reader(archivo, delimiter=',', skipinitialspace=False, strict=True)
    matrizVinculos = csvAMatriz(textoCSV)

    #Convertir matriz de los vínculos a matriz de probabilidades
    matrizProbabilidades = MatrizVinculosAMatrizProbabilidades(matrizVinculos)

    #Genera la matriz de teletransportación
    matrizTeletransportacion = MatrizDeTeletransportacion(len(matrizProbabilidades))

    #Factor de amortización.
    d = 0.85

    #Matriz de transición que representa al conjunto de páginas web
    matrizTransicion = MatrizDeTransicion(d, matrizProbabilidades, matrizTeletransportacion)

    #Se aplica el método de potencias para extraer el eigenVector de la matriz de transición
    #El eigenVector representa la importancia(relevancia) que tiene cada página web.
    eigenVector = PowerMethod(matrizTransicion, 0.0001)

    #Se despliegan los resultados obtenidos, se conserva el mismo orden establecido en el archivo csv.
    print(matrizTransicion)

if __name__ == "__main__":
    main()
