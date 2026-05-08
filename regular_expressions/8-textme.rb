#!/usr/bin/env ruby
File.readlines(ARGV[0]).each do |line|
sender = line.scan(/(\[from:\+\d{11}\])/).join 
receiver = line.scan(/(\[to:\+\d{11}\])/).join
flags = line.scan(/\[flags:-(\d{0,2}):(\d{0,2}):-(\d{0,2}):(\d{0,2}):-(\d{0,2})]/).join
end