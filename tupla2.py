#animales=("peroo","gato","raton","serpiente","caballo")
#print(animales[1:4])

#animales=("peroo","gato","raton")
#print(animales[0])

#animales=("peroo","gato","raton","serpiente","caballo")
#print(len(animales))#cuenta la cantidad de elementos

#las puthon tuples son inalterables, por lo que no pueden ser dotadas
#dotados de nuevos elementos. sin embargo, pra actualizar
#una tupla ya exixstente, puedes crear una tupla y añadir
#valores nuevos ademas de la tupla original. esto se hac e
#con el operador +.he aqui un ejemplo

#algunos_animales=(animales=("peroo","gato","raton","serpiente","caballo"))
#todos_los_animales=algunos_animales + ("hamster","jirafa")
#print(todos_los_animales)

#la funcion count, cuenta las veces que aparece un elelmto dentro
#una tupla de python
animales=("peroo","gato","raton","serpiente","caballo","peroo")
print(animales.count("peroo"))


#la funcion index, indica la pocicion en la que aparece un elemeto