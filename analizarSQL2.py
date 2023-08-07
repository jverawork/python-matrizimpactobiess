import re

def obtener_tablas_desde_sentencia_sql(sql):
    patron = r'\bSELECT\b\s+(.+\s)+?\bFROM\b\s+([a-zA-Z_]+\.?[a-zA-Z0-9_]*)|(?:,\s*)([a-zA-Z_][a-zA-Z0-9_]*)'
    resultados = re.findall(patron, sql, re.IGNORECASE)
    #tablas = [resultado[0] if resultado[0] else resultado[1] for resultado in resultados]
    return resultados

# Ejemplo de sentencia SQL
sentencia_sql = """
SELECT column1, column2, count(1), COUNT(*)
 INTO VNCONTADOR
FROM es.table_name1 t1, table_name2, 
table3 as t3, esquema.table4 t4, (select c1 from table5, table6 where dual) WHERE column3 = 5;
"""

# Obtener tablas desde la sentencia SQL
tablas = obtener_tablas_desde_sentencia_sql(sentencia_sql)
print("Tablas usadas:", tablas)