-- ghci -> iniciar repl
-- :l teste -> compilar
-- doubleMe 1 2 -> argumentos são separados por espaço
-- doubleUs 1 2 + doubleMe 3
doubleMe x = x + x
doubleUs x y = doubleMe x + doubleMe y
doubleSmallNumber x = if x > 100
                        then x
                        else x*2 -- Obrigatório do if
doubleSmallNumber' x = (if x > 100 then x else x * 2) + 1