"""
clase 13


lista=[];

lista.append("Fuchibol");
lista.append(45);

print(f"El nombre es: {lista[0]}");
print(f"La edad es: {lista[1]}");
bandera_sexo=True;
lista_numero=[];
while bandera_sexo:
    try:

        num=float (input("Ingresa un número para obtener su tabla de multiplicar: "));
        bandera_sexo=False;
    except ValueError:
        print("Dejate de joder peruanooooooooooooooooo");
    else:
        for i in range(10):
            i+=1;
            #si incorporamos int antes del cálculo el código cortará el número flotante y lo dejará convertido en un entero.
            lista_numero.append(int(num*i));

        print(f"{lista_numero}");
"""
"""
ingrese números enteros a una lista. Al ingresar un cero se detiene, además debe mostrar los elementos de ésta
 en forma ordenada ascendente.
"""
"""
lista=[];

while True:
    try:
        num=int(input("Ingresa muchos números: "));
    except:
        print("El número ingresado no es válido, intentalo nuevamente.");
    else:
        if num!=0:
            lista.append(num);
        else:
            print("El número ingresado es cero, saliendo...");
            break;
lista.sort();
print(lista);
"""

"""
Ingresar 10 números a una lista, luego muestre la suma y promedio de los elementos.

contador=0;
lista=[];
while True:
            if contador<10: 
                #con for no es óptimo, se cae cuando tira mensajes de error porque ocupan la pool de rangos.
                try:
                    num=float(input("Ingresa un número: "));
                except:
                    print("Tu mamá vende completos a 1500");
                else:
                    lista.append(num);
                    contador+=1;
            else:
                 break;

print(f"La suma de los números es: {sum(lista)}");
print(f"El promedio de los elementos es: {sum(lista)/(len(lista))}");
"""

"""
escriba un programa que permita almacenar 3 nombres solicitados por pantalla en una lista, 
luego el sistema debe mostrar por pantalla el nombre que tenga mayor cantidad de caracteres.
"""
lista_nombres=[];


for i in range(3):
    nombre=input("Ingresa un nombre: ");
    lista_nombres.append(nombre);
#Debemos comparar estos valores.    
lista_nombres.sort();
print(len(lista_nombres[0]));










