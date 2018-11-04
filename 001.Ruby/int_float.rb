n_int = 10
n_float = 10.0
n_strin = "10"

n_int.is_a? Integer # verificar se n é inteiro
n_float.is_a? Float 

"asdf".to_i # 0
"10".to_i # 10
10.to_s # "10"
10.to_f # 10.0
10.to_c # (10+0i)
10.to_r # (10/1)
42.even? # true
-12.abs # 12