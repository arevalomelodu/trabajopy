#coincidencias
import re

ex = re.compile("\d\d\d")
#ex = re.compile("\d\d\d\d")

cadena_uno = ex.search("curso de4927 python").group()
cadena_dos = ex.search("luid enrique4859arias").group()
cadena_tres = ex.search("curso de4927 python").group()

print(cadena_uno, cadena_dos, cadena_tres)