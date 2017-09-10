clear;
clc;

%Leer el archivo csv, sin los encabezados de filas y columnas
matrizVinculos = csvread('Ejemplos/Grafo1.csv',1,1);

%Por alguna extra�a raz�n lee una columna o fila de m�s, la cual contiene
%solamente 0's.
[m,n] = size(matrizVinculos);
if m~=n
    
    if m>n
        %Si tiene m�s filas que columnas
        matrizVinculos = matrizVinculos(1:n,:);
        N = n;
    else
        %Si tiene m�s columnas que filas
        matrizVinculos = matrizVinculos(:,1:m);
        N = m;
    end
end

%C�lculo de la matriz de probabilidades
matrizProbabilidades = zeros(N);
for i=1 : N
   suma = sum(matrizVinculos(:,i()));
   matrizProbabilidades(:,i) = matrizVinculos(:,i)/suma;
end

%Generaci�n de la matriz de teletransportacion
matrizTeletransportacion = ones(N)/N;

%C�lculo de la matr�z de transici�n
d = 0.85;
matrizTransicion = d*matrizProbabilidades + (1-d)*matrizTeletransportacion;
x = ones(N, 1);

%M�todo de las potencias
error = 0.000001;
dif = 1;
while(dif>error)
    y = matrizTransicion*x;
    xx = norm(y);
    y = y/norm(y);
    dif = sqrt(norm(y - x));
    x = y;
end

%%Otra formas de calcular el eigenvector:
%%V contiene una matriz con todos los eigenvectores
%%D contiene una matriz diagonal con todos los eigenvectores
%%La primer columna de V es la que nos interesa
%[V,D] = eig(matrizTransicion);

%Se presenta con porcentaje de relevancia
s = sum(x);
rank = (x/s)*100;
display(rank);


%--------------------------------------------------------------------------
% En internet se puede encontrar una versi�n simplificada del algoritmo
% A es la matriz de probabilidades, R es el eigenvector inicial
% d es el factor de amortizaci�n y epsilon es la diferencia m�nima para detener el
% metodo de potencias.
% function[R] = pagerank(A, R, d, epsilon)
%     [N,~] = size(A)
%     E=ones(N);
%     R_last = R;
%     delta=epsilon;
%     while (delta >= epsilon)
%         R = (d * A + (1-d)/N * E) * R_last;
%         dist=R-R_last;
%         delta = sqrt(dot(dist,dist));
%         R_last = R;
%     end