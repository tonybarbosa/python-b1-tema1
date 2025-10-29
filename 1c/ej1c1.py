"""
Enunciado
Implementa la función `mult_recursive(value, times)` que debe devolver el
resultado de sumar `value` `times` veces. Como puedes ver, su comportamiento
real es como si fuera una multiplicación. La función ha de ser implementada
usando recursividad. La función recibe dos parámetros:
 - value: un número entero, que representa el número a sumar
 - times: un número entero, que representa el número de veces que ha de sumarse `value` al resultado
Por ejemplo, si `value` vale 2 y `times` vale 3, la función ha de devolver 6, resultado sumar 2 + 2 + 2
Como puedes ver, su comportamiento real es como si fuera una multiplicación

Parámetros:
    value: número entero que se desea sumar
    times: número de veces que se desea sumar 'value'

Ejemplo:
    Entrada:
    value = 2
    times = 3

    Salida:
    6

Enunciat
Implementa la funció `mult_recursive(value, times)` que ha de tornar el
resultat de sumar `value` `times` vegades. Com podeu veure, el vostre comportament
real és com si fos una multiplicacióLa funció ha de ser implementada
usant recursivitat. La funció rep dos paràmetres:
- value: un name enter, que representa el número a sumar
- times: un name enter, que representa el name de vegades que s'ha de sumar `value` al resultat
Per exemple, si `value` val 2 i `times` val 3, la funció ha de tornar 6, resultat sumar 2 + 2 + 2

Paràmetres:
     value: name enter que es vol sumar
     times: name de vegades que es vol sumar 'value'

Exemple:
     Entrada:
     value = 2
     times = 3

     Sortida:
     6

"""


def mult_recursive(value, times):
    # Write here your code
#    print(value)
    if times == 1:

        return value
    else:
        return value + mult_recursive(value, times- 1)


# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
# Si vols provar el teu codi, descomenta les línies següents i executa l'script
if __name__ == "__main__":
    print("Must print 6: ", mult_recursive(2, 3))
