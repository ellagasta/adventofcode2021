#!/usr/bin/ruby
input = []
File.readlines('input.txt').each do |line|
  input << line.chomp
end

length = input.size
prev = input[0]
count = 0

input.each do |depth|
  count += 1 if depth > prev
  prev = depth
end

puts(count)
