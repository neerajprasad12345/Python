print("The Miles Per Gallon Program")
print()
choice="y"
while choice.lower()=="y":
    miles_driven=float(input("Enter the miles Driven:\t\t"))
    gallon_used=float(input("Enter the Gallon of Gas used:\t"))
    cost_per_gallon=float(input("Enter Cost per Gallon:\t\t"))
    print()
    miles_per_gallon=(miles_driven/gallon_used)
    total_gas_cost=(gallon_used*cost_per_gallon)
    cost_per_mile=(cost_per_gallon/miles_per_gallon)
    print("Miles Per Gallon:\t ",round(miles_per_gallon,2))
    print("Total Gas Cost:\t\t",round(total_gas_cost,2))
    print("Cost Per Miles:\t\t",round(cost_per_mile,1))
    print()
    choice=input("Wanna Continue(y/n)")
    print()
    print("THANK YOU")

