# Apuntes de Python

Los apuntes expuestos a continuación están basados en los datos de interés rescatados de las siguientes fuentes:

* Crash Course Python
* Proyectos personales
* Seminario de redes | Universidad Técnica Santa María

## Preámbulo 

Para comenzara trabajar con Python requerimos de su instalación, actualmente se trabaja únicamente con la versión 3 de Python debido a que la versión 2 se volvió obsoleta.

- Descargar Python: https://www.python.org/downloads/

## Aspectos esenciales

### Conceptos básicos

#### Strings

Las strings o cadenas de texto

#### Números

### Métodos básicos

Los métodos son acciones que pueden ser trabajados con distintas piezas de información, en este caso variables. Cada método esta seguido de unos paréntesis, esto es debido a que los métodos dependen de adicionar información adicional para funcionar.

#### Métodos matemáticos

```python
round(número, redondeo)		# Redondea un número a la cantidad deseada
abs(número)					# Devuelve el valor absoluto del número ingresado
max(10, 23, 12, 55)			# Obtienes el valor maximo de una serie de números ingresados
min(32, 99, 1, 123)			# Obtienes el valor mínimo de una serie de números ingresados
pow(base, potencia)			# Obtenemos la potencia de una número
```

#### Ingreso de datos en Python

Es posible permitir el ingreso de datos a los usuarios en Python mediante el método **input()**, al cual es posible añadir una descripción del valor a ingresar deseado. Todos los datos ingresados por este método son convertidos automáticamente a string.

```python
# Ingresar y almacenar valores

input("Ingresa un valor: ")	# Es ingresado un valor
valor = input("Ingresa un valor: ")	# Ingresamos un valor y lo guardamos en una variable
```

#### Modificar tipo de dato

Como se menciono anteriormente los valores ingresados mediante el método **input()** son almacenados en formato string, si deseamos cambiar esta limitación podemos utilizar la clase **int()** y el método **eval()**.

```python
### Modificar valores en Python ###

valor_str = input("\nIngresa un texto: ")
valor_int = int(input("Ingresa un número entero: "))
valor_float = float(input("Ingresa un número con decimales: "))
valor_eval = eval(input("Ingresa cualquier número : "))

print("\ninput() permite introducir strings | " + str(type(valor_str)))
print("int(input()) permite introducir números enteros | " + str(type(valor_int)))
print("float(input()) permite introducir floats | " + str(type(valor_float)))
print("eval(input()) permite introducir cualquier valor númerico y luego es almecenado según corresponda | " + str(type(valor_eval)) + "\n")
```

El resultado sería:

```
Ingresa un texto: carlos
Ingresa un número entero: 15
Ingresa un número con decimales: 22.2
Ingresa cualquier número : 92

input() permite introducir strings | <class 'str'>
int(input()) permite introducir números enteros | <class 'int'>
float(input()) permite introducir floats | <class 'float'>
eval(input()) permite introducir cualquier valor y luego es almecenado según corresponda | <class 'int'>
```

En el código es utilizado **type(valor_str)** para obtener el tipo de dato almacenado en una variable. Debido a que lo estamos mostrando por pantalla mediante el método **print()** debemos forzar su conversión a string con el método **str()**.

#### Cambiar Case de un string

Los métodos **upper()** y **lower()** modifican todas las palabras poniéndolas todas en minúsculas y mayúsculas respectivamente.

El método **title()** modifica cada palabra a formato de titulo, lo que provoca que cada letra comience con una mayúscula.

**Nota:** Guardar los valores de los strings en minúsculas es de mucha utilidad, para no tener problemas en la ejecución del programa y evitar confusiones con el usuario. Se recomienda utilizar estos métodos para presentar los datos convertidos al formato deseado.

```python
# Cambiar Case de un string

palabra = "carlos brignardello"
print("\nPalabras: carlos brignardello")
print("\nMétodo upper(): " + palabra.upper())
print("Método lower(): " + palabra.lower())
print("Método title(): " + palabra.title() + "\n")
```

```
Palabras: carlos brignardello

Método upper(): CARLOS BRIGNARDELLO
Método lower(): carlos brignardello
Método title(): Carlos Brignardello
```

#### Eliminar espacios laterales de un string

Pueden ser eliminados los espacios al comienzo y al final de un string utilizando los métodos **strip()**, **rstrip()** y **lstrip()**.

* Eliminar los espacios a la derecha: **rstrip()**
* Eliminar los espacios a la izquierda: **lstrip()**
* Eliminar los espacios laterales: **strip()**

```python
# Eliminar espacios laterales

palabra = " necesito espacio "
print("Palabra: " + palabra + "\n")
print("Método rstrip(): " + palabra.rstrip() +
	"\nMétodo lstrip(): " + palabra.lstrip() +
	"\nMétodo strip(): " + palabra.strip() + "\n")
```

```
Palabra:  necesito espacio

Método rstrip():  necesito espacio
Método lstrip(): necesito espacio 
Método strip(): necesito espacio
```

