'''Expresiones regulares
 Las expresiones regulares (1lamadas RE, o regex, o patrones de regex)
son esencialmente en un lenguaje de programación diminuto y altamente
especializado incrustado dentro de Python y disponible a través del módulo re.'''

import re #Importa el módulo re que proporciona funciones para trabajar con expresiones regulares en Python.
#sub_cadena = re.search("gh", "hola mundo!") #Output: None
sub_cadena = re.search(r"h", "hola mundo!") #Output: <re.Match object; span=(0, 1), match="h"> 
#sub_cadena = re.search(r"hola", "hola mundo!") #Output: <re.Match object; span=(0, 4), match='h'>
print (sub_cadena)


#La función search() de re se utiliza para buscar un patrón dado en una cadena. En este caso, estamos 
#buscando la subcadena "gh" dentro de la cadena "hola mundo!". El patrón de búsqueda se especifica utilizando una cadena de
#texto que se proporciona como el primer argumento. La r antes de la cadena indica una cadena de texto en bruto, lo que significa que los caracteres de escape se interpretan literalmente.
#El resultado de search() se almacena en la variable sub_cadena.''' 

#a función search() devuelve un objeto Match si se encuentra una coincidencia, o None si no se encuentra
#ninguna coincidencia. La salida en la consola mostrará el objeto Match si se encuentra una coincidencia,
#o None si no se encuentra ninguna coincidencia.'''