﻿"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
'''video_id,trending_date,title,channel_title,
category_id,publish_time,tags,views,likes,dislikes,
comment_count,thumbnail_link,comments_disabled,ratings_disabled
,video_error_or_removed,description,country'

'''
def newCatalog():
    catalog = {'title': None,
               'trending_date': None,
               'channel_title': None,
               'publish_time': None,
               'category_id': None,
               'views': None,
               'likes': None,
               'dislikes':None,
               'tags':None
               'country': None,}

    catalog['title'] = lt.newList()
    catalog['channel_title'] = lt.newList('SINGLE_LINKED',
                                    cmpfunction=comparechannels)
    catalog['tags'] = lt.newList('SINGLE_LINKED',
                                 cmpfunction=comparetagnames)
    catalog['trending_date'] = lt.newList('SINGLE_LINKED')
    catalog['publish_time'] = lt.newList('SINGLE_LINKED')
    catalog['category_id'] = lt.newList('SINGLE_LINKED',cmpfunction=comparectegoryid)
    catalog['views'] = lt.newList('SINGLE_LINKED')
    catalog['likes'] = lt.newList('SINGLE_LINKED')
    catalog['dislikes'] = lt.newList('SINGLE_LINKED')
    catalog['country'] = lt.newList('SINGLE_LINKED', cmpfunction=comparecountries)


    return catalog
# Funciones para agregar informacion al catalogo
def addBook(catalog, book):
    # Se adiciona el libro a la lista de libros
    lt.addLast(catalog['title'], book)
    # Se obtienen los autores del libro
    authors = book['authors'].split(",")
    # Cada autor, se crea en la lista de libros del catalogo, y se
    # crea un libro en la lista de dicho autor (apuntador al libro)
    for author in authors:
        addBookAuthor(catalog, author.strip(), book)
def addBookAuthor(catalog, authorname, book):
    """
    Adiciona un autor a lista de autores, la cual guarda referencias
    a los libros de dicho autor
    """
    authors = catalog['authors']
    posauthor = lt.isPresent(authors, authorname)
    if posauthor > 0:
        author = lt.getElement(authors, posauthor)
    else:
        author = newAuthor(authorname)
        lt.addLast(authors, author)
    lt.addLast(author['books'], book)
def addTag(catalog, tag):
    """
    Adiciona un tag a la lista de tags
    """
    t = newTag(tag['tag_name'], tag['tag_id'])
    lt.addLast(catalog['tags'], t)
# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento