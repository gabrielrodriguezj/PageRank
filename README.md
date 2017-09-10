# Breve descripción del algoritmo PageRank

Permite determinar la importancia o relevancia de una página web, dentro de un conjunto de páginas relacionadas o conectadas.

## Pasos del algoritmo
* 1.- Se define una cadena de Markov que describe el comportamiento de la navegación por las páginas de internet.
* 2.- Se calcula la matriz de probablidades-transicion, la cual contiene la probabilidad de que al visitar cierta página web, se pueda navegar hacia otra página a través de los vinculos que contiene dicha página.
* 3.- Se genera una matriz de teletransportación, de las mismas dimensiones que la matriz de transiciones, pero todos los elementos son igual a 1/numero de páginas de internet. Esta matriz representa la posibilidad que "tiene un usuario" de saltar de una página a otra. Esto va ayudar a que el método de potencias converja.
* 4.- Se genera una matriz de transiciones que es igual a d*(Matriz de probabilidades) + (1-d) * (Matriz de teletransportacion). Donde d=0.85, el factor de amortización.
* 5.- Se calcula el eigenvector de la matriz de transiciones con el metodo de potencias. El vector que resulte contendrá las ponderaciones asignadas a las páginas web, entre más alto sea este valor, significa que la página tiene una mayor relevancia.

## Autor
Gabriel de Jesús Rodríguez Jordán

## Bibliografía:
Coding The Matrix: Linear Algebra Through Computer Science Applications. Philip N. Klein.
