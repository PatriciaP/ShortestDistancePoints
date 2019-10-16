# ShortestDistancePoints
Problema dos pontos mais próximos

Dado um conjunto de pontos em um espaço bidimensional, encontre e imprima a distância entre os pontos mais próximos.
Entrada

O arquivo de entrada contém vários casos de teste. Cada caso de teste começa com um número inteiro N (0 ≤ N ≤ 10000), que denota o número de pontos neste conjunto. As N linhas seguintes contêm, cada uma delas, dois valores que são as coordenadas dos N pontos bidimensionais. O primeiro destes dois valores indica a coordenada X e o último indica a coordenada Y. A entrada é terminada por um conjunto cujo N = 0. Esta entrada não deve ser processada. O valor das coordenadas será um número não-negativo menor do que 40000. Exemplo:

3
0 0
10000 10000
20000 20000
5
0 2
6 67
43 71
39 107
189 140
0

Saída

Para cada conjunto de entrada imprima uma única linha de saída contendo um valor de ponto flutuante (com 4 dígitos após o ponto decimal) o qual denotará a distância entre os dois pontos mais próximos. Se não existirem tais dois pontos na entrada cuja distância for menor do que 10000, imprima a mensagem "INFINITY" sem as aspas.

INFINITY
36.2215
