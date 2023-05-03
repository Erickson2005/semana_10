'''Escribir un programa que pida al usuario una palabra y muestre por 
pantalla el número de veces que contiene cada vocal.'''

palabra = input("Introduce una palabra: ")
vocales = ['a', 'e', 'i', 'o', 'u']
for i in vocales: 
    times = 0
    for j in palabra: 
        if j == i:
            times += 1
    print("La vocal " + i + " aparece " + str(times) + " veces")
    
'''Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, 
Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada 
asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla 
las asignaturas que el usuario tiene que repetir.'''

materias = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
pasadas = []
for i in materias:
    nota = float(input("\nQué nota has sacado en " + i + " -> "))
    if nota >= 6:
        pasadas.append(i)
for j in pasadas:
    materias.remove(j)
print("Tienes que repetir " + str(materias))
