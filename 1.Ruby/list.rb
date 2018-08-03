lista = [1, 2, 3, 4]
new_lista = lista.collect { |x| 10 * x } # altera todos valores e retorna alterados
lista.map { |x| 2 * x } # [2, 4, 6, 8] não altera lista
# [1, 2, 3, 4]
lista.map! { |x| 2 * x } # [2, 4, 6, 8] altera a lista
# [2, 4, 6, 8]
["Cat", "Dog", "Bird"].include? "Dog"   # true

values = [1, 2, 3, 5, 8]

puts values.inject(:+) # => 19

ary = [1, "two", 3.0] #=> [1, "two", 3.0]
ary = Array.new    #=> []
Array.new(3)       #=> [nil, nil, nil]
Array.new(3, true) #=> [true, true, true]
Array.new(4) { Hash.new } #=> [{}, {}, {}, {}]
empty_table = Array.new(3) { Array.new(3) }
#=> [[nil, nil, nil], [nil, nil, nil], [nil, nil, nil]]
Array({:a => "a", :b => "b"}) #=> [[:a, "a"], [:b, "b"]]
arr = [1, 2, 3, 4, 5, 6]
arr[2]    #=> 3
arr[100]  #=> nil
arr[-3]   #=> 4
arr[2, 3] #=> [3, 4, 5]
arr[1..4] #=> [2, 3, 4, 5]
arr[1..-3] #=> [2, 3, 4]
arr.at(0) #=> 1
arr = ['a', 'b', 'c', 'd', 'e', 'f']
arr.fetch(100) #=> IndexError: index 100 outside of array bounds: -6...6
arr.fetch(100, "oops") #=> "oops"
arr.first #=> 1
arr.last  #=> 6
arr.take(3) #=> [1, 2, 3]
arr.drop(3) #=> [4, 5, 6]
browsers = ['Chrome', 'Firefox', 'Safari', 'Opera', 'IE']
browsers.length #=> 5
browsers.count #=> 5
browsers.empty? #=> false
browsers.include?('Konqueror') #=> false
arr = [1, 2, 3, 4]
arr.push(5) #=> [1, 2, 3, 4, 5]
arr << 6    #=> [1, 2, 3, 4, 5, 6]

a = []
a << 1 << 2 << 3 << 4 # [1, 2, 3, 4]

s1 = ["colors", "red", "blue", "green"]
s2 = ["letters", "a", "b", "c"]
s3 = "foo"
a = [s1, s2, s3]
a.assoc("letters") # [ "letters", "a", "b", "c" ]
a.assoc("foo") # nil

h = {"colors" => ["red", "blue", "green"], # hashes
     "letters" => ["a", "b", "c"]}
h.assoc("letters") # ["letters", ["a", "b", "c"]]
h.assoc("foo")  # nil

a, b, c = 1, 2, 3
(1..4).to_a = [1, 2, 3, 4]
%w{esse é um array de palavras}
# ["esse", "é", "um", "array", "de", "palavras"]

puts == p # true
print == p # true
puts "hello" # hello => com quebra de linha
p "hello" # hello => com quebra de linha
print "hello" # hello  => sem quebra de linha

Hash.new(0) # {}

# Symbols
h_s = {
  :simbol => "simbol"
}
h_s[:simbol] # "simbol"

h_s = {
  simbol: "simbol"
}
h_s[:simbol] # "simbol"

ary = [1,2,3,4,5]
ary.each do |i|
   puts i
end