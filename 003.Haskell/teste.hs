factorial :: (Integral a) => a -> a  
factorial 0 = 1
factorial 1 = 1
factorial n = n * factorial (n - 1) 