-- PL/SQL Block
BEGIN

  vncontador := 0;

  aocrespro := '0';
  aocmenerr := NULL;

  SELECT COUNT(*)
  INTO vncontador
  FROM tabla1
  WHERE CODOPEREC = aincodoperec
    AND SECREC    = ainsecrec;
    --AND CODFUN    = to_char(aiccodfun);

  IF vncontador = 0 THEN
    aocmenerr := 'La operacion ' || ainsecrec || ' no esta registrada en el sistema' ;
      RETURN;
  END IF;

  SELECT COUNT(*)
  INTO vncontador
  FROM tabla2, tabla3
  WHERE CODOPEREC = aincodoperec
    AND SECREC    = ainsecrec
    AND ESTOPE    = 'ANU';

for ind in (select * from tabla4)
loop
end loop

select * into v from tabla5 as t5;


  IF vncontador = 1 THEN
    aocmenerr := 'La operacion ' ||

select * into v from tabla6 joint tabla7;

select (select c1 from tabla8), c2 into v from tabla9;

