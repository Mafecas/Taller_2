#comentario de una línea 
#todo lo que va despues es ignorado por el 
#interprete de python

#variables:Espacio de memoria, con nombre,donde guardo valores 
#los nombres de variables deben ser cortos, descriptivo, NO TENER ESPACIOS 
# EN BLANCO ni caracteres especiaeles, no deben empezar por un número

#Descriptivo significa que representa la categoria del dato que quiero guardar
#En phyton las variables pueden contener cualquier dato de tipo primitivo
#números (entero,reales), cadenas de caracteres (string), booleanos (true,false)
#caracteres(letras)

variable=1
Variable='juventud divino tesore, te vas para no volver, cuando quiero llorar'
variable=True
Variable='a'
Variable=3.1415926535


#para asignar un valor a una variable se usa el operador =

#operadores:Mecanismos para obtener un dato a partir de otros datos.
#los datos que intervienen se llaman 

#Aritmeticos: +-*/%
#De comparación: Retornan True or False. > < >= <= == !=
#Los de logica booleana:OR AND. Retornan True or False de acuerdo a una
#tabla de verdad.Los operadores siempre son bolaneos(True or False)

a=True
b=False

print(a and b)




#2.Repetir la ejecucion de un bloque de 
#3.

#Sentencia if. si se cumple una condicion (se evalua como true)
#se ejecuta un loque de código


entrada= int (input ("cuantos años tiene"))

if entrada<18:
    print("Es un menor de edad.")
else:
    print("ya esta grande,deje de chillar")
    
#Taller crear un programa que genere un numero aleatorio 
#Entre 2 y 12. si el numero es 7 imprimir ganó 