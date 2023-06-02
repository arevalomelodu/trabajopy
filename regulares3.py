import re

#sub_cadena= re.search("\d\d\d","hola789mundo57!")
# con el comando \d\d\d estoy buscando tres números consec
#sub_cadena = re.search(r"\d\d", "hola789mundo57!")
sub_cadena = re.search(r"\d\d", "hola7mundo57!")
print (sub_cadena.group())

