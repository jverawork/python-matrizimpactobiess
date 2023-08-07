import re

cadena = "Mi color favorito es [rojo] y [azul] es mi segundo favorito."

patron = r'\[([^\]]+)\]\s*favorito'

coincidencias = re.findall(patron, cadena, re.IGNORECASE)

if coincidencias:
    print("Colores favoritos encontrados:", coincidencias)
else:
    print("No se encontraron coincidencias")
import re

cadena = "Mi color favorito es [rojo] y [azul] es mi segundo favorito."

patron = r'\[([^\]]+)\]\s'

coincidencias = re.findall(patron, cadena, re.IGNORECASE)

if coincidencias:
    print("Colores favoritos encontrados:", coincidencias)
else:
    print("No se encontraron coincidencias")

patron = r          '\bSELECT\b\s+(((.+)\s+))+?\bFROM\b\s+([A-Z_][A-Z0-9_]*.{0,1}\w+)\s*(;|\)?)'
patron = r'([\s]+|\()\bSELECT\b\s.*\s+\bFROM\b\s[\w\s,]*\s*(;|\))'