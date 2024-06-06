#Función sumar dos números con parametros y sin retorno
def suma_de_dos_numeros(num1,num2):
    suma=num1+num2;
    print(suma);
#Función restar dos números con parametros y sin retorno
def resta_de_dos_numeros(num1,num2):
    resta=num1-num2;
    print(resta);
def multiplicacion_de_dos_numeros(num1,num2):
    multiplicacion=num1*num2;
    print(multiplicacion);
def division_de_dos_numeros(num1,num2):
    if num2 != 0:
        division=num1/num2;
        print(division);
    else:
        print("No se puede dividir por cero!");

#Crear un sistema de administración de productos de una Ferretería
#Función para agregar productos.
#Función para mostrar productos.
#Función para buscar productos.
#Función para eliminar productos.


lista_productos=["hacha","martillo","tornillo","esmeril"];

def agregar_productos():
    producto=input("Ingresa un producto");
    lista_productos.append(producto);
    print("El producto se ingresó correctamente.");

def mostrar_productos():
    print(f"La lista de productos es: {lista_productos}");

def buscar_productos(producto):
    if producto in lista_productos:
        print("El producto se encuentra en la lista");
        return True;
    else:
        print("El producto no está en la lista");
        return False;

def eliminar_productos():
    producto=input("Ingresa un producto para eliminarlo");
    lista_productos.remove(producto);
    print(f"El producto {producto} se ha eliminado");


