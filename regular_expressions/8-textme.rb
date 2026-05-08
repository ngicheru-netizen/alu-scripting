#!/usr/bin/env ruby
line = ARGV[0]
sender = line.scan(/\[from:([^\]]+)\]/).join
receiver = line.scan(/\[to:([^\]]+)\]/).join
flags = line.scan(/\[flags:([^\]]+)\]/).join
puts "#{sender},#{receiver},#{flags}"
