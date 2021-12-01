#!/usr/bin/ruby
def main
  input = []
  File.readlines('input.txt').each do |line|
    input << line.chomp.to_i
  end

  length = input.size
  window_size = 3
  prev = depth_window_sum(input, 0, window_size)
  count = 0

  (0..length-window_size).each_with_index do |_, i|
    cur = depth_window_sum(input, i, window_size)
    count += 1 if cur > prev
    prev = cur
  end

  puts(count)
end

def depth_window_sum(array, index, window_size)
  return array[index...index+window_size].sum
end

main
