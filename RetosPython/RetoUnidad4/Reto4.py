from functools import reduce

positivos_C19 = {
    'Colombia ': { 
        'Risaralda ': [( 'Pereira ', 45) , (' Dosquebradas ', 15) , ('La Virginia ', 30) ], 
        'Quindio ': [( 'Armenia ', 75) , ('Montenegro ', 86) ]},
    'Mexico ': {
        'Quintana Roo ': [( 'Benito Juarez ', 34) , (' Solidaridad ',56) ],
        'Nayarit ': [( 'Compostela ', 23) , ('San Blas ', 35) , ('Xalisco ', 74) , ('Del Nayar ', 46) ]}
}

def analizaPacientes(opt: int, db: dict, pais: str = ''):
    if opt == 1 or opt == 2:
        try:
            x = db[pais]
        except KeyError:
            return 'La opción ingresada requiere de un país valido'

    if opt == 0:
        pais = pais.strip()
        if pais != '':
            return 'La opción no recibe país'
        promedio = []
        nombres = []
        for pais in db:
            nombres.append(pais)
            suma_pais = 0
            cantidad = 0
            for departamento in db[pais]:
                lista = list(map(lambda x: x[1], db[pais][departamento]))
                suma_pais += int(reduce(lambda x, y: x+y, lista))
                cantidad += len(lista)
            promedio.append(round(suma_pais / cantidad, 2))
        return dict(zip(nombres, promedio))
    elif opt == 1:
        promedio = []
        nombres = []
        for departamento in db[pais]:
            nombres.append(departamento)
            lista = list(map(lambda x: x[1], db[pais][departamento]))
            suma_dep = int(reduce(lambda x, y: x+y, lista))
            promedio.append((round(suma_dep/len(lista), 2)))
        return dict(zip(nombres, promedio))
    elif opt == 2:
        promedio = []
        nombres = []
        mayor = ('', 0)
        for departamento in db[pais]:
            for ciudad in db[pais][departamento]:
                if ciudad[1] > mayor[1]:
                    mayor = ciudad
        return mayor
    else:
        return 'La opción no es valida'

print ( analizaPacientes (0 , positivos_C19 ))
print ( analizaPacientes (1 , positivos_C19 , 'Mexico '))
print ( analizaPacientes (2 , positivos_C19 , 'Mexico '))
print ( analizaPacientes (2 , positivos_C19 , 'Colombia '))
print ( analizaPacientes (5 , positivos_C19 ))

