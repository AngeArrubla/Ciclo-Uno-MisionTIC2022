import json
import pandas as pd
import numpy as np


def preProcesado(DF):
    # Funcion que prepara los generos en un DF para ser codificadas en la matriz
    # Devuelve tambien los generos en una lista
    categoriasDF = DF['categories'].apply(pd.Series)
    categoriasDF['business_id'] = DF['business_id']
    categoriasDF = categoriasDF.drop_duplicates(['business_id'])
    categoriasDF . set_index('business_id', inplace=True)
    categories = [categoriasDF[categorie].unique()
                  for categorie in categoriasDF.columns]
    categories = [categorie for lista in categories for categorie in lista if all
                  ([pd.isnull(categorie) == False, categorie != ' ', categorie != '', len(
                      str(categorie)) > 1])]
    categories = list(set(categories))
    return categoriasDF, categories


def codificaMatriz(DF, genres: list, producto: list):
    indices = []
    nueva_serie = []

    for i in producto:
        if type(i) == str:
            indices.append(genres.index(i))
    for i in genres:
        nueva_serie.append(0)
    for i in indices:
        nueva_serie[i] = 1
    data = np.array(nueva_serie)
    ser = pd.Series(data)
    return ser


def recomiendaNegocio(url_puntuacion: str, url_perfil: str, url_recomendacion: str) -> json:
    a = pd.read_json(url_perfil)
    b = preProcesado(a)
    c = {}

    a_2 = pd.read_json(url_recomendacion)
    b_2 = preProcesado(a_2)
    c_2 = {}

    puntajes = pd.read_csv(
        url_puntuacion,
        sep=';',
        names=['usuario', 'puntuacion'])
    puntajes = puntajes.set_index('usuario')

    for i in range(0, len(b[0])):
        c[b[0].index[i]] = codificaMatriz(b, b[1], b[0].iloc[i]).to_list()
    d = pd.DataFrame(c, b[1])
    for i in range(0, len(b[0])):
        d[b[0].index[i]] = puntajes.loc[b[0].index[i]
                                        ]['puntuacion'] * d[b[0].index[i]]
    suma = d.to_numpy().sum()
    perfil = []
    for i in b[1]:
        perfil.append(d.loc[i].sum() / suma)
    d['Perfil'] = perfil

    for i in range(0, len(b_2[0])):
        c_2[b_2[0].index[i]] = codificaMatriz(
            b_2, b_2[1], b_2[0].iloc[i]).to_list()
    d_2 = pd.DataFrame(c_2, b_2[1])

    coincidencias = []
    nueva_serie = []
    nuevos_indices = []

    for i in range(0, len(d)):
        if d.index[i] in d_2.index.tolist():
            coincidencias.append(d.index[i])

    for i in range(0, len(d_2)):
        nueva_serie.append(0)
    for i in coincidencias:
        nuevos_indices.append(d_2.index.tolist().index(i))
    for i in nuevos_indices:
        valor = d.loc[d_2.index[i]]['Perfil']
        nueva_serie[i] = valor
    d_2['Perfil'] = nueva_serie

    for i in d_2:
        if i != 'Perfil':
            d_2[i] = d_2[i] * d_2['Perfil']

    sumatorias = []
    i_sumatorias = []
    for i in d_2:
        if i != 'Perfil':
            if d_2[i].sum() != 0:
                sumatorias.append(round(d_2[i].sum(), 5))
                i_sumatorias.append(i)
    serie_sumatorias = pd.Series(sumatorias, index=i_sumatorias)
    serie_sumatorias = serie_sumatorias.sort_values(ascending=False)
    result = serie_sumatorias.to_json()
    parsed = json.loads(result)
    return(json.dumps(parsed, indent=4))