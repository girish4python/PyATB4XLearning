# TASK2
# Create a program , take 2 inputs from the user num1, num2 and give them
# max
# pow num1 to num2
# sub, mul, sum, div.
# Format your out with f{""}


a = int(input("Enter Number 1 :  "))
b = int(input("Enter Number 2 : "))

Max_num=max(a,b)
print(f"Maximum number is {Max_num}")

Power =pow(a,b)
print(f"Power of number is {Power}")

sub = a - b
print(f"sub is {sub}")

mul = a * b
print(f"mul is {mul}")

sum = a + b
print(f"sum is {sum}")

div = a/b
print(f"div is {div}")
