# 2023 Semestre 1

## Instrucciones Generales
- El archivo **debe** llamarse **Examen1.py**
- **Debe** respetar el nombre de las funciones y el nombre de los parámetros que más adelante se describen
- **Debe** construir las funciones con **Python**
- **Debe** utilizar la programación vistas en clases **while for if elif**
- **Debe** crear los comentarios de cada función tomando en cuenta **Nombre**, **Entrada**, **Salida** y **Restricciones**

- Cada pregunta vale 10 puntos:
  - Los comentarios 2 puntos (2 cometario bueno, 1 comentario incompleto, 0 no hay comentarios)
  - Desarrollo de las validaciones de las restricciones 2 puntos
  - Algoritmo 6 puntos (6 Excelente, 5 a 1 Termiando con errores de sintaxis o incompleto , 0 No lo hizo)

## 1.	Número Hermano (10 puntos) 

Escriba un programa con sintaxis Python cuya función principal se llame **numeroHermano(num)**, que reciba como entrada un **número entero positivo** denominado num y que retorne si cumple (True) o no los requisitos (False) de número hermano. Un número hermano es un número natural y que posee dos divisores primos (el 1 no es primo):

Ejemplos del comportamiento de la función:

```python
>>>numeroHermano(20) #(divisores propios: 2, 4, 5, 10)
True
>>> numeroHermano(8) #(divisores propios: 2,4)
False
>>> numeroHermano(-8)
"Error en la entrada, debe ser número positivo"
```
## 2.	Número Polimax (10 puntos) 

Escriba un programa con sintaxis Python cuya función principal se llame **numeroPolimax(num)**, recibe un número entero cualquiera e indique si el número es un Número Polimax. Un número es Polimax si al dividir en dos el número, sus dos partes tienen la misma cantidad de impares y pares. El parámetro “num” debe de tener un largo PAR.
Ejemplos del comportamiento de la función:

```python
>>> numeroPolimax(4312) #(43 y 12)
True 
>>> numeroPolimax(32707) #(327 y 707)
True
>>> numeroPolimax(-6887) #(68 y 87)
False
>>> numeroPolimax(-9) #(9 y 9)
True

```

## Formar Numero (10 puntos) 

Escriba un programa con sintaxis Python cuya función principal se llame **formarNumero(lista)**, recibiendo una **lista de números enteros** como parámetro de entrada y debe formar un nuevo número. Si al menos aparece **un número negativo**, la respuesta debe ser negativo
Ejemplos del comportamiento de la función:

```python
>>> formarNumero ([9, 15, 894])  
915894
>>> formarNumero ([0, 2, 0, -1258, 0, 1])
-20125801
```

## Validador de Secuencia (10 puntos) 

Escribir un programa con sintaxis Python cuya función principal se llame **validarSecuencia(num, grupo, llave)**, recibe tres parámetros el primero “numero” será el valor a evaluar, el segundo “grupo” será la cantidad de dígitos a recorrer y tercero “llave” será el valor a verificar. Para retornar True, si la suma de todos los dígitos de más a la izquierda del grupo de números creados es igual al valor de “llave”. Ejemplos del comportamiento de la función:
- Sea el número 258645125
- Grupo 3 y,
- Llave 9
- Se recorre en grupos de 3 generando los números 258, 645 y 125 
- De ellos se sumará solo el dígito de más a la izquierda, es decir 2 + 6 + 1 = 9
- La suma es 9 y es igual al valor del parámetro de llave, por lo tanto, es True

Cómo restricciones:
- Todos los valores deben ser enteros
- Tanto llave y grupo deben ser positivos

```python
>>> validarSecuencia (258645125, 3, 9)
True
>>> validarSecuencia (256412, 4, 9) #En este caso la suma sería solo 6
False
>>> validarSecuencia (45280731, 1, 30)
True
```

