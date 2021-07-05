import random
Array = [random.randint(-100, 100) for i in range(30)]
MaxNumber = max(Array)

print(Array)
print("Max number is " + str(MaxNumber))
print("Index is " + str(Array.index(MaxNumber)))
print("Numbers that are nearby and < 0")
u = 0

for i in range(29):
  if Array[i]<0 and Array[i+1]<0:
    print("Numbers : " + str(Array[i]) + " and " + str(Array[i+1]))
    u = 1
if u == 0:
	print("There are no such numbers")