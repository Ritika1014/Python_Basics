
import dirmodule

print("Number Range Checker")
print("=" * 20)

# Get range boundaries from user
min_range = float(input("Enter the minimum value of the range: "))
max_range = float(input("Enter the maximum value of the range: "))

# Get number to check
number = float(input("Enter a number: "))

# Check if number is in range
if min_range <= number <= max_range:
    print(f"✓ The number {number} is WITHIN the range [{min_range}, {max_range}]")
else:
    print(f"✗ The number {number} is OUTSIDE the range [{min_range}, {max_range}]")

print("Done!")
print(f"Imported module 'dirmodule' contains: {dir(dirmodule)}")


