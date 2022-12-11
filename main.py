import pandas as pd # Importa pandas y usa un alias para poder utilizar sus recursos

def main():
    #1 Cargar como dataframe de pandas el csv imdb_titulos.csv y mostrar sus 5 primeros registros
    titulos_de_peliculas = pd.read_csv('imdb_titulos.csv')
    print(titulos_de_peliculas.head(5))

    #2 Cargar como dataframe de pandas el csv imdb_elenco.csv y mostrar sus 5 primeros registros
    elenco = pd.read_csv('imdb_elenco.csv')
    print(elenco.head(5))

    #3 Mostrar el número de registros del dataframe de titulos
    print("El número de registros del dataframe de titulos es: {} ".format(len(titulos_de_peliculas.shape)))

    #4 Mostrar el número de registros del dataframe de elenco
    print("El número de registros del dataframe de elenco es: {} ".format(len(elenco.shape)))

    #5 Mostrar las 5 peliculas más antiguas del listado de titulos
    print(titulos_de_peliculas.sort_values(by='year').head(5))

    #6 Mostrar las peliculas que en el titulo tienen la palabra "Dracula". También mostrar el número total de peliculas que coincidan con este requisito
    print(titulos_de_peliculas[titulos_de_peliculas['title'].str.contains('Dracula')])
    print("Las peliculas que en el titulo tienen la palabra Dracula y que coinciden con este requisito son: {} peliculas ".format(len(titulos_de_peliculas[titulos_de_peliculas['title'].str.contains('Dracula')])))

    #7 Mostrar los 10 titulos más comunes (que más se repiten)
    print(titulos_de_peliculas['title'].value_counts().head(10))

    #8 Mostrar cual fue la primer pelicula hecha titulada "Romeo and Juliet"
    print(titulos_de_peliculas[titulos_de_peliculas['title'] == 'Romeo and Juliet'].sort_values(by='year').head(1))

    #9 Listar todas las peliculas que contengan la palabra "Exorcist" ordenadas de la más vieja a la más reciente
    print(titulos_de_peliculas[titulos_de_peliculas['title'].str.contains('Exorcist')].sort_values(by='year'))

    #10 Mostrar cuantas peliculas fueron hechas en el año 1950
    print("Las peliculas que fueron hechas en el año 1950 son: {} peliculas ".format(len(titulos_de_peliculas[titulos_de_peliculas['year'] == 1950])))

    #11 Mostrar cuantas peliculas fueron hechas de 1950 a 1959
    print("Las peliculas que fueron hechas de 1950 a 1959 son: {} peliculas ".format(len(titulos_de_peliculas[(titulos_de_peliculas['year'] >= 1950) & (titulos_de_peliculas['year'] <= 1959)])))

    #12 Mostrar todos los roles o papeles que hubo en la pelicula "The Godfather". También mostrar el número total de coincidencias
    print("Los roles o papeles que hubo en la pelicula The Godfather son: {}", elenco[elenco['title'] == 'The Godfather'])
    print("El número total de coincidencias que hubo en la pelicula The Godfather son: {} ".format(len(elenco[elenco['title'] == 'The Godfather'])))

    #13 Mostrar el elenco completo ordenado por la clasificacion "n" de la pelicula "Dracula" de 1958
    print("El elenco completo ordenado por la clasificacion 'n' de la pelicula 'Dracula' de 1958 es: ",elenco[(elenco['title'] == 'Dracula') & (elenco['year'] == 1958)].sort_values(by='n'))

    #14 Mostrar cuantos papeles de "Bruce Wayne" han sido hechos en la historia de las peliculas
    print("Los papeles de Bruce Wayne que han sido hechos en la historia de las peliculas son: {} papeles ".format(len(elenco[elenco['character'] == 'Bruce Wayne'])))

    #15 Mostrar cuantos papeles ha hecho "Robert De Niro" en su carrera
    print("Los papeles que ha hecho Robert De Niro en su carrera son: {} papeles ".format(len(elenco[elenco['name'] == 'Robert De Niro'])))

    #16 Listado de papeles como protagonista (n=1) que tuvo el actor "Charlton Heston" en la década de los 60's, ordenado por año de forma descendente
    print("El listado de papeles como protagonista (n=1) que tuvo el actor Charlton Heston en la década de los 60's, ordenado por año de forma descendente es: ",elenco[(elenco['name'] == 'Charlton Heston') & (elenco['n'] == 1) & (elenco['year'] >= 1960) & (elenco['year'] <= 1969)].sort_values(by='year', ascending=False))

    #17 Mostrar cuantos papeles para actores hubo en la década de los 50's
    print("Los papeles para actores que hubo en la década de los 50's son: {} papeles ".format(len(elenco[(elenco['type'] == 'actor') & (elenco['year'] >= 1950) & (elenco['year'] <= 1959)])))

    #18 Mostrar cuantos papeles para actrices hubo en la década de los 50's
    print("Los papeles para actrices que hubo en la década de los 50's son: {} papeles ".format(len(elenco[(elenco['type'] == 'actress') & (elenco['year'] >= 1950) & (elenco['year'] <= 1959)])))

    return None

if __name__ == '__main__':
    main()

