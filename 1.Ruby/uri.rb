lista0 = []

def numeric(str)
  # https://stackoverflow.com/questions/14551256
  if (str =~ /[0-9]/) == 0
    return true
  else
    return false
  end
end

for i in 0...gets.to_i
  s = gets.to_s.strip
  lista = [s[2, 2], s[5, 3], s[-2, 2]]
  n = 0

  lista.each do |i|
    if i.length == 3
      if not(numeric(i[1]))
        n += (i[0].to_i + i[2].to_i)
      else
        n += i.to_i
      end
    else
      n += i.to_i
    end
  end
  lista0 << n
end

lista0.each do |a|
  puts(a)
end
