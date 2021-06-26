def abstracta (lado: int, cubos: int) -> tuple:

    areaCubo = lado*lado*6*cubos
    volumenCubo = lado ** 3 * cubos
    resultado=(lado,areaCubo,volumenCubo)
    
    return resultado
'''
print("caso de prueba 1:", abstracta (41 , 9))
print ("caso de prueba 2", abstracta (26 , 9))
print ("caso de prueba 3", abstracta (17 , 9))
'''

def suma(valor1:float,valor2:float,valor3:float):

    resultado = valor1 + valor2 + valor3
    resta = (valor2-valor1)
    return resultado



a=suma(1,2,3)
b=abstracta(a,4)
print(b)

def prueba(a: int, b: int, c: int):
    suma = a + b
    resta = b - a
    multiplicacion = a * c
    resultado = suma + multiplicacion
    return resta