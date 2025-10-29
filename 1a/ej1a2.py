'''
Enunciado:
Crea una función 'sum_odd_numbers(list_numbers)' que reciba como 
parámetro una lista de números positivos enteros llamada 'list_numbers'
y devuelva la suma de los números impares encontrados en la lista.
Considerar que 'list_numbers' debe contener valores numéricos enteros mayores
o iguales a '0', en caso contrario se debe mostrar un error tipo 'ValueError'.

El error lo puedes mostrar con la siguiente instrucción:    
raise ValueError("MENSAJE DE ERROR")

Parámetros:
- list_numbers: Lista de números enteros positivos.

Ejemplo:
    Entrada:
    sum_odd_numbers([1, 2, 3, 4, 5, 10, 21, 100])

    Salida:
    30

Enunciat:
Crea una funció 'sum_odd_numbers(list_numbers)' que rebi com
paràmetre una llista de nombres positius enters anomenada 'list_numbers'
i torneu la suma dels números imparells trobats a la llista.
Considereu que 'list_numbers' ha de contenir valors numèrics enters majors
o iguals a '0', en cas contrari cal mostrar un error tipus 'ValueError'.

L'error el pots mostrar amb la següent instrucció:
raise ValueError("MISSATGE D'ERROR")

Paràmetres:
- list_numbers: Llista de nombres enters positius.

Exemple:
     Entrada:
     sum_odd_numbers([1, 2, 3, 4, 5, 10, 21, 100])

     Sortida:
     30

'''

def sum_odd_numbers(list_numbers):
    # Write here your code
    suma=0
    for numero in list_numbers:
        if not isinstance(numero,int):
            raise ValueError("Los numeros deben ser del tipo int")
        elif numero < 0:
            raise ValueError("los numeros deben ser mayores de cero")
        elif numero%2:
            suma +=numero
           
    # print(suma)
    return(suma)

# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script 
# Si vols provar el teu codi, descomenta les línies següents i executa l'script
print(sum_odd_numbers([1, 2, 3, 4, 5, 10, 21, 100]))
