#!/usr/bin/env julia

const GLOBALS = Dict(:empCount=>0)
                  
            
struct Employee    
    name::String   
    salary::Float64
   
    function Employee(name::AbstractString, sal::Real)
        GLOBALS[:empCount] += 1
        new(name, sal)
    end
end


display_employee_count() = println("Total Employees: $(GLOBALS[:empCount])")
# could also  do
# display_count(::Type{Employee})

function Base.show(io::IO, emp::Employee)
    println(io, "Employee (Name: $(emp.name), Salary: $(emp.salary))")
end
   

emp1 = Employee("Zara", 2000)
emp2 = Employee("Manni", 5000)

show(emp1)
show(emp2)

display_employee_count()