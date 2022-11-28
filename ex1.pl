idade(O,crianca):-O<12.
idade(O,crianca):-O=12.
idade(O,adole):-O>12.
idade(O,adole):-O=18.
idade(O,adulto):-O>18.
idade(O,adulto):-O=65.

?idade(32,adulto).
