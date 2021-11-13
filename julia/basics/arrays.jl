#!/usr/bin/env julia

nums = [1,2,3,4]

for i in nums
	println(i)
end

function myfun(x)
	println("myfun:",x)
end

function anotherfun(y)
	println("another fun: ",y)
end


function thirdfun(z)
	println("this is z: ",z)
end

# Can put functions in an array
analyses = [myfun,anotherfun,thirdfun]
for f in analyses
	f(99)
end

push!(nums,22)

println(nums)
