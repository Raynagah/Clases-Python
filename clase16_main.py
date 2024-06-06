#Archivo principal
import funciones_clase16 as funciones
"""
flag=True;
print("¡Bienvenido al menú de funciones aritméticas básicas!");
while flag:
    try:
        num1=int(input("Ingresa un número: "));
        num2=int(input("Ingresa otro número: "));
    except:
        print("Los números ingresados no son válidos, intentalo nuevamente");
    else:
            flag=False;
            print("Ahora seleccione una de las siguientes opciones para utilizar los números ingresados:\n");
            print("1.Sumar dos números");
            print("2.Restar dos números");
            print("3.Multiplicar dos números");
            print("4.Dividir dos números");
            print("5.Salir del programa");
            while True:
                try:
                    opcion=input("Ahora selecciona una opción del menú:");
                except:
                    print("Error, la opción ingresada no es válida!!");
                else:
                    if opcion=="1":
                        print("Elegiste sumar dos números");
                        funciones.suma_de_dos_numeros(num1,num2);
                    elif opcion=="2":
                        print("Elegiste restar dos números");
                        funciones.resta_de_dos_numeros(num1,num2);
                    elif opcion=="3":
                        print("Elegiste multiplicar dos números");
                        funciones.multiplicacion_de_dos_numeros(num1,num2);
                    elif opcion=="4":
                        print("Elegiste dividir dos números");
                        if num2!=0:
                            funciones.division_de_dos_numeros(num1,num2);
                        else:
                            print("Error, no se puede dividir por cero");
                    elif opcion=="5":
                        print("Elegiste salir del programa\n");
                        break;
                    else:
                        print("La opción ingresada no es válida");




funciones.resta_de_dos_numeros(num1,num2);
funciones.multiplicacion_de_dos_numeros(num1,num2);
funciones.division_de_dos_numeros(num1,num2);
"""
lista_productos=["hacha","martillo","tornillo","esmeril"];
while True:
    
    print("Bienvenido a la Ferretería!!");
    print("Elija una de las siguientes opciones");
    print("1.Agregar productos");
    print("2.Mostrar los productos");
    print("3.Buscar productos");
    print("4.Eliminar un producto/s");
    try:
        opcion=input("Ingresa tu opción: ");
    except:
        print("La opción ingresada no es válida, intentalo nuevamente...");
    else:
        if opcion=="1":
            print("Elegiste agregar un producto");
            producto_nuevo=input("Ingresa el producto que deseas agregar");
            if producto_nuevo not in lista_productos:
                funciones.agregar_productos(producto_nuevo);
            else:
                print("El producto ya se encuentra en la lista, ingrese otro!");
        elif opcion=="2":
            funciones.mostrar_productos();
        elif opcion=="3":
            producto=input("Ingrese el producto que desea buscar: ");
            funciones.buscar_productos(producto);
        elif opcion=="4":
            producto=input("Ingrese el producto que desea eliminar: ")
            funciones.eliminar_productos(producto);
            
def eliminar_producto():
    print()

"""
Utilizando la función de buscar producto se debe hacer la de eliminarlo si es que está dentro de la lista. (utilizando return)
"""