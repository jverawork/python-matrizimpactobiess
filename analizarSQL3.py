sentencia_sql = ''
with open('sentenciaplsql.sql', 'r') as archivo:
        sentencia_sql = archivo.read()

import re

def obtener_tablas_desde_sentencia_sql(sql):
    patron = r'\bSELECT.+\b FROM\b\s+(([A-Z_][A-Z0-9_]+\.?[A-Z0-9_]*)|(?:,\s*))+[.\s]*[;]'
    patron = r'([\s]+|\()\bSELECT\b\s.*\s+\bFROM\b\s([\w\s,])*'
    patron = r'\bSELECT\b(.|\s)+?(?=FROM)+?\bFROM\b\s+(([A-Z_]\w*\.?[A-Z_]*(\w|\.)*)|(?:\s+AS\s+\w+)|(\s*,\s*)|(?:\s+\w+))+(?:WHERE)?'
    resultados = re.findall(patron, sql, re.IGNORECASE)
    #tablas = [resultado[0] if resultado[0] else resultado[1] for resultado in resultados]
    return resultados

# Obtener tablas desde la sentencia SQL
tablas = obtener_tablas_desde_sentencia_sql(sentencia_sql)
print("Tablas usadas:", tablas)
#\bSELECT\b(.|\s)+?(?=FROM)+?\bFROM\b\s+(([A-Z_]\w*\.?[A-Z_]*(\w|\.)*)|(?:\s+AS\s+\w+)|(\s*,\s*)|(?:\s+\w+))+(?=WHERE)?


\bSELECT\b(.|\s)+?(?=FROM)+?\bFROM\b\s+(([A-Z_]\w*\.?[A-Z_]*\w*)|(?:,\s*))+
(\bSELECT\b\s+(((.+)\s+))+?\bFROM\b\s+(([A-Z_]\w*\.?[A-Z_]*\w*)(?:\s*\w*)?|(?:,\s*))+)(?=WHERE)?
 
 ([\s]+|\()\bSELECT\b\s+(((.+)\s+))+?\bFROM\b\s+[A-Z_](\w*|\s|,)*(((.+)\s+))+?
   \bSELECT\b\s+(((.+)\s+))+?\bFROM\b\s+([A-Z_][A-Z0-9_]*.{0,1}\w+)\s*(;|\)?)
   \bSELECT\b\s+(((.+)\s+))+?\bFROM\b

   ([\s]+|\()\bSELECT\b\s.*\s+\bFROM\b\s[\w\s,]*\s*(;|\))
     
     
  SELECT COUNT(*)
  INTO VNCONTADOR
  FROM ESQUEMA.TABLA1
  WHERE CODOPEREC = AINCODOPEREC
    AND SECREC    = AINSECREC;
    --AND CODFUN    = TO_CHAR(AICCODFUN);

  IF VNCONTADOR = 0 THEN
    AOCMENERR := 'LA OPERACION ' || AINSECREC || ' NO ESTA REGISTRADA EN EL SISTEMA' ;
      RETURN;
  END IF;

  SELECT COUNT(*)
  INTO VNCONTADOR
  FROM TABLA2 T2, ESQUEMA.TABLA3 T3
  WHERE CODOPEREC = AINCODOPEREC
    AND SECREC    = AINSECREC
    AND ESTOPE    = 'ANU';

FOR IND IN (
  SELECT  * 
  FROM TABLA4 T4 
	WHERE A=B
	) 
	LOOP
	LOOP
END LOOP

SELECT * INTO V FROM TABLA5 AS T5;


  IF VNCONTADOR = 1 THEN
    AOCMENERR := 'LA OPERACION ' ||

SELECT * INTO V FROM TABLA6 JOINT TABLA7;

SELECT (
SELECT C1 FROM TABLA8) A, C2 INTO V FROM TABLA9;

SELECT * INTO V FROM TABLA10 ;

SELECT * INTO V FROM TABLA11, ESQUEMA.TABLA12;

SELECT * INTO V FROM ESQUEMA.TABLA11, TABLA12;

DELETE FROM TABLADELETE1 WHERE T1=T2;

SELECT C1 FROM TABLA13;

SELECT * INTO V FROM ESQUEMA.TABLA14 T, TABLA15 T5;
