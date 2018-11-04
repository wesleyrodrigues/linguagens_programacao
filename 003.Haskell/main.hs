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
boomBangs xs = [ if x < 10 then "BOOM!" else "BANG!" | x <- xs, odd x]
length' xs = sum [1 | _ <- xs] -- _ igual elixir
removeNonUppercase st = [ c | c <- st, c `elem` ['A'..'Z']]