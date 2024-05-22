"""
w3schools.com para estudiar de manera autónoma.

Lista=muchos valores
Matriz=son listas anidadas mediante corchetes

lista=["hola","chao","juan"];
#la i tomará los valores dentro de la lista y cada vez que itere mostrará una de las palabras que se encuentran en dicha lista.
for i in lista:
    print(i);

"""
rango=range(5);
texto="Hola Mundo";

lista_deportes=["Fútbol","Rugby","Basquetball","HandBall"];
matriz_numerica=[[1,2,3],
                 [4,5,6],
                 [7,8,9]];

#for que recorre e imprime un rango de valores numéricos [0,1,2,3,4]
print("\n1) For utilizando Range(5)");
for elemento in rango:
    print(elemento,end=" - ");

#for que recorre e imprime un rango de caracteres [Hola Mundo]
print("\n2) For utilizando Texto");
for elemento in texto:
    print(elemento,end=" - ");

#for que recorre e imprime una lista [Fútbol,Rugby,Basquetball,Handball]
print("\n3) For utilizando Lista");
for elemento in lista_deportes:
    print(elemento,end=" - ");

#for que recorre e imprime una matriz [[1,2,3]]
print("\n4) For utilizando Matriz");
for elemento in matriz_numerica:
    for elemento2 in elemento:
            print(elemento2,end=" - ");
    
        
    
             


















