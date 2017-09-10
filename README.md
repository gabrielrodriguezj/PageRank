# Breve descripción del algoritmo PageRank

Permite determinar la importancia o relevancia de una página web, dentro de un conjunto de páginas relacionadas o conectadas.

## Pasos del algoritmo
* 1.- Se define una cadena de Markov que describe el comportamiento de la navegación por las páginas de internet. Aquí es importante aclarar que ninguna columna puede estar con puros 0's, ya que esto llevará a una violación de las cadenas de markov: En la matriz de probabilidades, la suma de todas las columnas debe ser igual a 1.
* 2.- Se calcula la matriz de probablidades-transicion, la cual contiene la probabilidad de que al visitar cierta página web, se pueda navegar hacia otra página a través de los vinculos que contiene dicha página.
* 3.- Se genera una matriz de teletransportación, de las mismas dimensiones que la matriz de transiciones, pero todos los elementos son igual a 1/numero de páginas de internet. Esta matriz representa la posibilidad que "tiene un usuario" de saltar de una página a otra. Esto va ayudar a que el método de potencias converja.
* 4.- Se genera una matriz de transiciones que es igual a d*(Matriz de probabilidades) + (1-d) * (Matriz de teletransportacion). Donde d=0.85, el factor de amortización.
* 5.- Se calcula el eigenvector de la matriz de transiciones con el metodo de potencias. El vector que resulte contendrá las ponderaciones asignadas a las páginas web, entre más alto sea este valor, significa que la página tiene una mayor relevancia.

## Estructura del archivo csv
El grafo de la estructura de las páginas web se debe escribir en un archivo CSV, el cual contendrá en los encabezados de filas y columnas los nombres de las páginas web.

En una columna X, se anotan los vínculos hacía las otras páginas que contiene X (en la fila que corresponda). Por ejemplo, si la página A contiene tres vínculos, uno hacía B, otro hacía D, y otro hacía F, la columa A contendría un 1, en la fila B, en la fila D y en la fila F.

Si una página no contiene vínculos hacía otra (pero otras páginas sí tienen hacía ella), se debe agregar un 1 en la fila y columna de la página en cuestión. Por ejemplo, la página A no contiene vínculos a otras páginas, en la fila A, columna A se debe incluir 1, esto con el fin de cumplir con una de las reestricciones de las cádenas de Markov.

## Autor
Gabriel de Jesús Rodríguez Jordán

## Bibliografía:
Coding The Matrix: Linear Algebra Through Computer Science Applications. Philip N. Klein.
