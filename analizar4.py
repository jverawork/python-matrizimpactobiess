import re

cadena = "SELECT (SELECT C1 FROM TABLA8 t8, tabla81) , C2 INTO V FROM TABLA9 t9;"
cadena = "SELECT (SELECT C1 FROM TABLA8) , C2 INTO V FROM TABLA9;"

patronsubcadena = r'\(\s*(?<=\sFROM)\s+(\w+)'
patron = r'\s*(?<=\sFROM)\s+(\w+)'

resultados1 = re.findall(patronsubcadena, cadena, re.IGNORECASE)
resultados2 = re.findall(patron, cadena, re.IGNORECASE)

print("patronsubcadena : ", resultados1)
print("patron : ", resultados2)
