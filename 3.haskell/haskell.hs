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

-- ghci> let lostNumbers = [4,8,15,16,23,48]
-- ghci> lostNumbers -> [4,8,15,16,23,48] --> Só aceita um tipo em listas (Ex int).
-- ghci> [1,2,3,4] ++ [9,10,11,12] -> [1,2,3,4,9,10,11,12]  
-- ghci> "hello" ++ " " ++ "world" -> "hello world"  
-- ghci> ['w','o'] ++ ['o','t']    -> "woot" 
-- ghci> 'Q':" GATINHA" -> "Q GATINHA"  
-- ghci> 5:[1,2,3,4,5]  -> [5,1,2,3,4,5]
-- ghci> "Steve Buscemi" !! 6            -> 'B'  --> retornando um número por index
-- ghci> [9.4,33.2,96.2,11.2,23.25] !! 1 -> 33.2 --> retornando um número por index
-- ghci> head [5,4,3,2,1] -> 5
-- ghci> tail [5,4,3,2,1] -> [4,3,2,1]
-- ghci> last [5,4,3,2,1] -> 1
-- ghci> init [5,4,3,2,1] -> [5,4,3,2] --> retorna tudo com exceção do último elemento.
-- ghci> length [5,4,3,2,1] -> 5
-- ghci> null [1,2,3] -> False  
-- ghci> null []      -> True
