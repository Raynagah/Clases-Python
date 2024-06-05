#Idealmente, dejar las funciones dentro de un archivo aparte para luego llamarlas...
#...en el archivo principal
"""
Funciones

-Con parámetros
-Sin parámetros
-Con retorno
-Sin retorno
"""
#ejemplo de una función sin parámetros y sin retorno.

def sumar_dos_numeros():

    num1=int(input("Ingresa un número: "));
    num2=int(input("Ingresa otro número: "));
    suma=num1+num2;
    print(f"La suma es: {suma}");
#Llamar a la función sin parámetros
#sumar_dos_numeros();

#ejemplo de una función con parámetros y con retorno
def sumar_dos_numeros_parametros(num1,num2):
    suma=(num1+num2);
    print(f"La suma es: {suma}");

#Llamar a la función con parámetros
#sumar_dos_numeros_parametros(8,23);


#ejemplo de una función sin parámetros y con retorno.

def sumar_dos_numeros_retorno():

    num1=int(input("Ingresa un número: "));
    num2=int(input("Ingresa otro número: "));
    suma=num1+num2;
    return suma;
#Llamar a la función con retorno
#suma=sumar_dos_numeros_retorno();
#print(f"El resultado de la suma es: {suma}");


#ejemplo de una función con parámetros y con retorno.

def sumar_dos_numeros_parametro_y_retorno(num1,num2):
    suma=num1+num2;
    return suma;
#Llamar a la función con parámetros y con retorno
#suma=sumar_dos_numeros_parametro_y_retorno(5,10);
#print(f"El resultado de la suma es: {suma}");










