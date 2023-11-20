# Actividad 3 | Daniel Trejo Camacho | Universidad del Valle de México | Ciencia de Datos

# Ejercicios 1 a 3
class Actividades:
    def __init__(self):
        self = self

    # Ejercicio 1: El siguiente método evalua si un número es par o impar:
    def impar_o_par(self, num1):
        # Se comprueba si el residuo de una divisón es 0.
        if (num1 % 2) == 0:
            return "El número {} es par".format(num1)
        else:
            return "El número {} es impar".format(num1)
    
    # Ejercicio 2: El siguiente método ayuda a determinar si un estudiante se encuentra acreditado o no:
    def calificación(self, grade):
        # Se comprueba cuál ha sido la calificación obtenida por el estudiante y se asigna retroalimentación
        if grade > 10 or grade < 0:
            return "Error"
        elif grade == 10:
            return "Excelente"
        elif grade == 9:
            return "Muy bien"
        elif grade == 8:
            return "Bien"
        elif grade == 7:
            return "Regular"
        elif grade >= 0 and grade <= 6:
            return "No acreditado"
        
    # Ejercicio 3: El siguiente método comprueba si los números de una lista son pares o impares
    def impar_o_par_lista(self, list1):
        # Se crea un ciclo for en el cual se accede a cada elemento de la lista.
        my_list = []

        # Se comprueba si el elemento de lista es par o impar)
        for n in list1:
            if (n % 2) == 0:
                my_list.append("El número {} es par".format(n))
            elif (n % 2) != 0:
                my_list.append("El número {} es impar".format(n))
        # Los resultados se guardan en una lista auxiliar y se imprime el resultado por pantalla.
        return my_list

# Ejercicio 1.1: Se prueba la funcionalidad del primer método (número par)
# Se crea el objeto 
mi_número = Actividades()
# Se llama al método y se da interactividad a la función
# Si se ingresa el número 2 el resultado será "El número 2 es par".
print(mi_número.impar_o_par(int(input("Ingresa un número: "))))

# Ejercicio 2.1: Se prueba la funcionalidad del segundo método (calificación)
calificación = Actividades()
# Se llama al método y se da interactividad a la función
# Si se ingresa el número 10 el resultado será "Excelente"
print(calificación.calificación(int(input("Ingresa una calificación: "))))

# Ejercicio 3.1: Se prueba la funcionalidad del tercer metodo (impar_o_par_lista)
mi_lista = Actividades()
print(mi_lista.impar_o_par_lista([3, 2, 6]))

##############
# Ejercicio 4: estructuras de repetición

# Se crea un diccionario que almacene el número de item (key) y su precio (value).
# El diccionario se crea fuera de la clase con la finalidad de facilitar su atualización.
items = {"item1": 15, "item2": 100, "item3": 30}

class Ejercicio_4: # Se crea la clase que contendrá los métodos necesarios para la actividad.
    def __init__(self, items):
        self.items = items
    
    # Se crea un método que contará el número de items que el usario compra con base a un diccionario.
    def núm_of_items(self, my_items):
        # Se crea una lista auxiliar que contendrá los textos resultantes del ciclo.
        items_comprados = []

        # Se busca qué items se han comprado y la cantidad.
        for key in my_items.keys():
            items_comprados.append("Usted ha comprado {} unidades del artículo {}".format(my_items[key], key))

        for element in items_comprados:
            # Retornamos los elementos de la lista uno por uno para imprimirlos por pantalla.
            return element
    
    # Se crea un método que retornará el valor total de compra con base al diccionario del usario. 
    def total_cost(self, my_items):
        # Se crea una variable 0 que contendrá el precio total de los items adquiridos.
        total = 0

        # Se obtiene el "código" de cada item comprado (almacenado en las keys del diccionario)
        for key in my_items.keys():
            # Se cumprueba que el item comprado exista en la lista de items.
            if key in items.keys():
                # Se multiplica la cantidad comprada por el valor unitario.
                total += (my_items[key] * self.items[key])
            else:
                # Si el item no existe simplemente no lo contemplará.
                pass

        # El total de cada item se va sumando en la variable auxiliar y se retorna el valor total (tras la finalziación del ciclo)
        return total

# Ejercicio 4.1: Se prueba la funcionalidad de la clase "Ejercicio_4"

# Se crea el objeto con el diccionario de items a la venta
customer1 = Ejercicio_4(items)

# Se define la compra del primer cliente
customer1_purchase = {"item1": 2, "item3": 4}

# Retorna el total de objetos comprados
print(customer1.núm_of_items(customer1_purchase))

# Retorna el total a pagar
print("El total a pagar es: " + str(customer1.total_cost(customer1_purchase)) + " MXN")