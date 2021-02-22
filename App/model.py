"""
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
    catalog = {'videos':None, 'categories':None}
    catalog['videos'] = lt.newList()
    #catalog['categories'] = lt.newList(delimeter='')
    return catalog
# Funciones para agregar informacion al catalogo
def addtitle(catalog, title):
    # Se adiciona el libro a la lista de libros
    lt.addLast(catalog['videos'], title)
    # Se obtienen los autores del libro
    channel_title = title['channel_title']
    # Cada autor, se crea en la lista de libros del catalogo, y se
    # crea un libro en la lista de dicho autor (apuntador al libro)
    addtitlechannel(catalog, channel_title.strip(), title)
def addtitlechannel(catalog, channelname, title):
    """
    Adiciona un autor a lista de autores, la cual guarda referencias
    a los libros de dicho autor
    """
    channels = []
    channel=None
    for video in catalog['videos'].values():
        if type(video)==dict:
            for info in video.values():
                if info != None:
                    print(info,'\n')#,info['channel_title'])
                    channel=info['channel_title']
                    if channel not in channels:
                        channels.append(channel)
    '''
    poschannel = lt.isPresent(channels, channelname)
    if poschannel > 0:
        channel = lt.getElement(channels, poschannel)
    else:
        channel = newchannel(channelname)
        lt.addLast(channels, channel)
    lt.addLast(channel['titles'], title)
def addTag(catalog, tag):
    t = newTag(tag['tag_name'], tag['tag_id'])
    lt.addLast(catalog['tags'], t)
# Funciones para creacion de datos
def newchannel(name):
    channel = {'name': "", "titles": None}
    channel['name'] = name
    channel['titles'] = lt.newList('SINGLE_LINKED')
    return channel
# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista
def comparechannels(channelname1, author):
    if (channelname1.lower() in channel['name'].lower()):
        return 0
    return -1
# Funciones de ordenamiento'''