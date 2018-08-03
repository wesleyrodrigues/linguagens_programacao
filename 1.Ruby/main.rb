# irb terminal
2**3            # 8
1.0 == 1        # true
1.0.eql?(1)     # false
1 <=> 1         # 0
1 <=> 2         # -1
2 <=> 1         # 1
(1..10) === 10  # true
(1...10) === 10 # false
# equal? for object
1/2 # 0

3.times { puts "Hello!" } # Hello!/nHello!/nHello!

local_v   # Local Variable
@inst_v   # Instance Variable
@@class_v # Class Variable
$global_v # Global Variable
ClassN    # Class Name
CONST_N   # Constant Name     

Time.now.thursday? # true

for i in 0...gets.to_i
  puts i
end

for i in 1..gets.to_i
  puts i
end