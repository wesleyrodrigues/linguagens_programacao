# irb terminal

class ClassName
  def fun
    # algo
  end
end

a = 1

3.times { puts "Hello!" } # Hello!/nHello!/nHello!

s1 = ["colors", "red", "blue", "green"]
s2 = ["letters", "a", "b", "c"]
s3 = "foo"
a = [s1, s2, s3]
a.assoc("letters") # [ "letters", "a", "b", "c" ]
a.assoc("foo") # nil

h = {"colors" => ["red", "blue", "green"],
     "letters" => ["a", "b", "c"]}
h.assoc("letters") # ["letters", ["a", "b", "c"]]
h.assoc("foo")  # nil

a = gets.chomp # input sem quebra de linha
b = gets # input com quebra de linha

n = 10
n.is_a? Integer # verificar se n é inteiro

