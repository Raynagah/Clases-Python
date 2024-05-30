"""
Resolución actividad día Lunes
"""
import random;
import time;

lista=[];
lista_usuario=[];
lista_ganadora=[];
contador=0;

print("\nBienvenido a Lotería Vargas\n");
while contador<5:
    num=int(input("Ingresa tus 5 números de la suerte: "));
    lista_usuario.append(num);
    contador+=1;
print(f"\nSus números de la suerte son: {lista_usuario}");

for lista in range(5):
    while True:
        num_aleatorio=random.randint(1,21);
        time.sleep(1);
        print(f"Se generó el siguiente número: {num_aleatorio}");
        if num_aleatorio not in lista_ganadora:
            lista_ganadora.append(num_aleatorio);
            break;

print(f"Los números de la lista ganadora son: {lista_ganadora}");

for x in lista_usuario:
    if x in lista_ganadora:
        print(f"Usted ha acertado en: {x}");
        contador+=1;

if contador==5:
    print("Usted se ganó la Lotería. \n!!!!!FELICIDADES!!!!!!");
else:
    print("Usted no ganó. Viva la ludopatía!!!!");






















