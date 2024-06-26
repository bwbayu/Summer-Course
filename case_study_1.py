gallons_used = float(input("Enter the gallons used (-1 to end): "))
gallons_sum = 0
miles_sum = 0

while gallons_used != -1:
    miles_driven = float(input("Enter the miles driven: "))
    miles_per_gallon = miles_driven/gallons_used
    print(f"The miles/gallons for this tank was {miles_per_gallon:.6f}")
    gallons_sum += gallons_used
    miles_sum += miles_driven
    gallons_used = float(input("Enter the gallons used (-1 to end): "))
    
miles_per_gallon_avg = miles_sum/gallons_sum
print(f"The overall average miles/gallon was {miles_per_gallon_avg:.6f}")