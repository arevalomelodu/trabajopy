import re 
sub_cadena = re.search(r"jx", "hola mundo!")

#print (sub_cadena.group()) #El mensaje de error "group" is not a known

                            #member of "None" indica que se está intentando #acceder al método group() en un objeto None.
                            # if sub_cadena is not None:
if sub_cadena is not None:
    print(sub_cadena.group())

else:
    print("No se encontró ninguna coincidencia.")