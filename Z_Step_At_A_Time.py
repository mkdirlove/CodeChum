x = int(input("Enter an integer for x: "))
y = int(input("Enter an integer for y: "))
z = int(input("Enter an integer for z: "))

output = ""
for i in range(x, y + 1, z):
    output += str(i) + ", "

# Remove the trailing comma and space
output = output[:-2]

print(output)

