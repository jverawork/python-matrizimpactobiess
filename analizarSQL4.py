import re

cadena = "Ejemplo: (SELECT C1 FROM TABLA1) , C2 INTO V FROM TABLA9;"

patron = r'[\s]+|\()\bSELECT\b\s.*\s+\bFROM\b\s([\w\s,]*TABLA1[\w\s,]*)\s*(;|\))'

coincidencia = re.search(patron, cadena)

if coincidencia:
    contenido = coincidencia.group(2)
    print("Contenido entre FROM y TABLA1:", contenido)
else:
    print("No se encontraron coincidencias")
