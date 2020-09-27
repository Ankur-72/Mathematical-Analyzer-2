print("Hey there!")
print("What's your name?")
name = input(str())
print("Hey " + name)
print("Please enter the range of your numbers")
print("Starting point:")
#start = input(int())
start = int(input())
print("Ending point:")
#end = input(int())
end = int(input())

print("The following numbers are even numbers within these limits:")
for x in range(start,end,1):
	if x%2 == 0:
		print(x)

print("The following numbers are odd numbers within these limits:")
for x in range(start,end,1):
	if x%2:
		print(x)